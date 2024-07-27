from concurrent import futures
import grpc
import test_pb2
import test_pb2_grpc
import time

class HeaderServiceServicer(test_pb2_grpc.HeaderServiceServicer):
    def SendComplexData(self, request, context):
        print("Received data:")
        # for key, hdr in request.headers.items():
        #     print(f"Header {key}: values={hdr.values}, timestamp={hdr.timestamp.seconds}, details={hdr.details}")
        start_time = request.start_time
        current_time = time.time()
        delay = current_time -start_time
        print(f"Start time: {delay}")
        return test_pb2.Empty()

def serve():
    options = [
        ('grpc.max_receive_message_length', 10 * 1024 * 1024),  # 메시지 최대 크기를 10MB로 설정
        ('grpc.max_send_message_length', 10 * 1024 * 1024)  # 전송 메시지 최대 크기도 10MB로 설정
    ]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=options)
    test_pb2_grpc.add_HeaderServiceServicer_to_server(HeaderServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()