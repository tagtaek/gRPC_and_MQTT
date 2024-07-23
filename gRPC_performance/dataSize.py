import json

large_array = [i for i in range(12500000)]
json_array = json.dumps(large_array)
array_size = len(json_array)
total_size = array_size * 5
print(f"Size of one large array: {array_size} bytes")
print(f"Total size of 10 arrays: {total_size} bytes")