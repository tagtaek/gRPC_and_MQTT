import grpc
import time
import json
import os
import perform_pb2
import perform_pb2_grpc

os.environ["GRPC_MAX_RECEIVE_MESSAGE_LENGTH"] = str(1000 * 1024 * 1024)
os.environ["GRPC_MAX_SEND_MESSAGE_LENGTH"] = str(1000 * 1024 * 1024)

def run():
    channel = grpc.insecure_channel('localhost:50051', options=[
        ('grpc.max_send_message_length', 1024 * 1024 * 1000),
        ('grpc.max_receive_message_length', 1024 * 1024 * 1000),
    ])
    stub = perform_pb2_grpc.SendServiceStub(channel)
    large_array = [i for i in range(12500000)]

    start_time = time.time()

    for i in range(1, 6):
        message = {
            'data': large_array,
            'start_time': start_time
        }
        data = perform_pb2.Message(data=json.dumps(message))
        stub.SendData(data) # transfer to server
    
    print(f'complete')

if __name__ == '__main__':
    run()

    # https://zzang9ha.tistory.com/346
    # 커밋 시, 파란색 리포지토리 오류 해결 방법