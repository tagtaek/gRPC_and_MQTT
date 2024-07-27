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