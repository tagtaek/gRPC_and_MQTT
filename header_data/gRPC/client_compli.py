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
        headers = {
            'header' + str(i): json.dumps({
                "values": ["value" + str(i), "additional" + str(i)],
                "timestamp": time.time(),
                "details": {
                    "sub_key1": "sub_value1_" + str(i),
                    "sub_key2": "sub_value2_" + str(i)
                }
            }) for i in range(50000)  # 복잡한 헤더 데이터 (9.5MB)
        }
        metadata = [(key, value) for key, value in headers.items()]
        message2 = {
            'start_time': start_time
        }
        message = header_pb2.MyData(data=json.dumps(message2))
        stub.SendData(message, metadata=metadata)

if __name__ == '__main__':
    run()