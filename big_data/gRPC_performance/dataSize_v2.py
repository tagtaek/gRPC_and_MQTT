import json
import random
import time
import os

def generate_complex_data(index):
    data = {
        "user": {
            "id": index,
            "name": f"User {index}",
            "email": f"user{index}@example.com",
            "address": {
                "street": f"{index} Main St",
                "city": "Anytown",
                "state": "CA",
                "zipcode": f"{12345 + index}"
            },
            "phones": [
                {"type": "home", "number": f"555-{1234 + index}"},
                {"type": "work", "number": f"555-{5678 + index}"}
            ],
            "preferences": {
                "newsletter": bool(random.getrandbits(1)),
                "notifications": random.sample(["email", "sms", "push"], 2)
            },
            "history": [
                {"timestamp": "2024-01-01T12:00:00Z", "event": "login"},
                {"timestamp": f"2024-01-02T{15 + index}:00:00Z", "event": "purchase", "details": {"item": "Laptop", "price": 1200 + index}}
            ]
        },
        "transaction": {
            "id": f"txn_{index:03d}",
            "amount": random.uniform(100, 500),
            "currency": "USD",
            "items": [
                {"product_id": f"prod_{index:03d}", "quantity": random.randint(1, 5), "price": random.uniform(50, 200)},
                {"product_id": f"prod_{index + 1:03d}", "quantity": random.randint(1, 5), "price": random.uniform(50, 200)}
            ],
            "payment_method": {
                "type": "credit_card",
                "provider": random.choice(["Visa", "MasterCard", "Amex"]),
                "card_number": "**** **** **** 1234",
                "expiration": "12/25"
            },
            "status": "completed",
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
    }
    return data

def generate_json_file(index):
    data = generate_complex_data(index)
    file_name = f'complex_file_{index}.json'
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
    return file_name

# 하나의 파일 생성 및 크기 측정
file_name = generate_json_file(0)
file_size = os.path.getsize(file_name)
print(f"File size of {file_name}: {file_size} bytes")

# 총 6개의 파일을 생성할 때 예상 용량
total_size = file_size * 6
print(f"Estimated total size for 6 files: {total_size} bytes")
