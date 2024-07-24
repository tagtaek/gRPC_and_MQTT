import grpc
import header_pb2
import header_pb2_grpc
import time
import json

def run():
    options = [
        ('grpc.max_metadata_size', 64 * 1024 * 1024)  # 메타데이터 최대 크기를 32KB로 설정
    ]
    start_time = time.time()
    with grpc.insecure_channel('localhost:50051', options=options) as channel:
        stub = header_pb2_grpc.SendserviceStub(channel)
        metadata = [('header-key-' + str(i), 'header-value-' + str(i)) for i in range(200000)] # 6MB
        message2 = {
            'start_time': start_time
        }
        message = header_pb2.MyData(data=json.dumps(message2))
        stub.SendData(message, metadata=metadata)

if __name__ == '__main__':
    run()