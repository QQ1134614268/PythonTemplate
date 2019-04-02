import json

data = {"code":10000, "data":0}
print(type(data))
data = json.dumps(data)
print(type(data))
data = json.loads(data)
print(type(data))
print(data['data'])

str1 = '{"a":1, "b":2}'
print(type(str1))
data = json.loads(str1)
print(type(data))
