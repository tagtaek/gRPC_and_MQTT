from concurrent import futures
import grpc
import header_pb2
import header_pb2_grpc
import time
import json

class SendServiceServicer(header_pb2_grpc.SendserviceServicer):
    def SendData(self, request, context):
        message = json.loads(request.data)
        start_time = message['start_time']
        current_time = time.time()
        delay = current_time - start_time
        # 메타데이터 파싱 및 출력
        for key, value in context.invocation_metadata():
            try:
                metadata_content = json.loads(value)
                print(f"Received complex header {key}: {metadata_content}")
            except json.JSONDecodeError:
                print(f"Received header {key}: {value}")

        print(f'Message delay: {delay} seconds')
        return header_pb2.Empty()

def serve():
    options = [
        ('grpc.max_metadata_size', 64 * 1024 * 1024)
    ]
    server = grpc.server(futures. ThreadPoolExecutor(max_workers=10), options=options)
    header_pb2_grpc.add_SendserviceServicer_to_server(SendServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()