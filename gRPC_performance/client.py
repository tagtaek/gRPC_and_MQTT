import grpc
import time
import json
import perform_pb2
import perform_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = perform_pb2_grpc.SendServiceStub(channel)

    start_time = time.time()

    for i in range(1, 10001):
        message = {
            'data': i,
            'start_time': start_time
        }
        data = perform_pb2.Message(data=json.dumps(message))
        stub.SendData(data) # transfer to server
        print(f'Sent message {i}')

if __name__ == '__main__':
    run()

    # https://zzang9ha.tistory.com/346
    # 커밋 시, 파란색 리포지토리 오류 해결 방법