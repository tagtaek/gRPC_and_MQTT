import grpc
from concurrent import futures
import time
import complicated_pb2
import complicated_pb2_grpc

class SendService(complicated_pb2_grpc.SendServiceServicer):
    def SendData(self, request, context):

        # 다양한 데이터 타입
        # print(f'Text: {request.text}')
        # print(f'Number: {request.number}')
        # print(f'Float Number: {request.float_number}')
        # print(f'Flag: {request.flag}')
        # print(f'String List: {request.string_list}')
        # print(f'String Map: {request.string_map}')
        # print(f'Nested Text: {request.nested.nested_text}')
        # print(f'Nested Number: {request.nested.nested_number}')

        current_time = time.time()
        delay = current_time - request.start_time
        print(f'Message delay: {delay} seconds')

        return complicated_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_receive_message_length', 1000 * 1024 * 1024),
        ('grpc.max_send_message_length', 1000 * 1024 * 1024)
    ])
    complicated_pb2_grpc.add_SendServiceServicer_to_server(SendService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()