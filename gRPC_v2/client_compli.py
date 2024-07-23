import grpc
import time
import complicated_pb2
import complicated_pb2_grpc

def run():
    options = [
        ('grpc.max_receive_message_length', 1000 * 1024 * 1024),  # 1000MB
        ('grpc.max_send_message_length', 1000 * 1024 * 1024)
    ]
    channel = grpc.insecure_channel('localhost:50051', options=options)
    stub = complicated_pb2_grpc.SendServiceStub(channel)

    # 다양한 데이터 타입을 포함하는 큰 데이터 생성
    text = "A" * 50 * 1024 * 1024 # 50MB text data
    number = 123456
    float_number = 12345.6789
    flag = True
    string_list = ["string_{}".format(i) for i in range(2500000)] # 33MB
    string_map = {"key_{}".format(i): "value_{}".format(i) for i in range(2000000)} # 43.8MB
    nested = complicated_pb2.NestedMessage(nested_text="Nested Text", nested_number=789)

    start_time = time.time()

    request = complicated_pb2.Message(
        text=text,
        number=number,
        float_number=float_number,
        flag=flag,
        string_list=string_list,
        string_map=string_map,
        nested=nested,
        start_time=int(start_time)
    )

    response = stub.SendData(request)

    print("sending is completed.")

if __name__ == '__main__':
    run()