import grpc
from concurrent import futures
import time
import json
import perform_pb2
import perform_pb2_grpc

class SendService(perform_pb2_grpc.SendServiceServicer):
    def SendData(self, request, context):
        message = json.loads(request.data)
        start_time = message['start_time']
        current_time = time.time()
        delay = current_time - start_time
        print(f'Message {message["data"]} delay: {delay} seconds')
        return perform_pb2.Empty() # response is empty message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    perform_pb2_grpc.add_SendServiceServicer_to_server(SendService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(36400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

## 수정 필요!!!