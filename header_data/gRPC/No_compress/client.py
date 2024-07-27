import grpc
import test_pb2
import test_pb2_grpc
import time
from google.protobuf.timestamp_pb2 import Timestamp

def run():
    options = [
        ('grpc.max_receive_message_length', 10 * 1024 * 1024),  # 메시지 최대 크기를 10MB로 설정
        ('grpc.max_send_message_length', 10 * 1024 * 1024)  # 전송 메시지 최대 크기도 10MB로 설정
    ]
    with grpc.insecure_channel('localhost:50051', options=options) as channel:
        stub = test_pb2_grpc.HeaderServiceStub(channel)
        start_time=time.time()
        headers = {
            'header' + str(i): test_pb2.ComplexHeader(
                values=["value" + str(i), "additional" + str(i)],
                timestamp=Timestamp(seconds=int(time.time())),
                details={'sub_key1': 'sub_value1_' + str(i), 'sub_key2': 'sub_value2_' + str(i)}
            ) for i in range(50000)
        }
        message = test_pb2.ComplexData(
            headers=headers,
            start_time=start_time
        )
        response = stub.SendComplexData(message)
        print("Data sent successfully.")

if __name__ == '__main__':
    run()