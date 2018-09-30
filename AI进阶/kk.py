import json
data = {"a":1,"b":2}
print(type(data))
d = {"a":1,"b":2}
print(type(d))
print(d)
f = json.dumps(d)
print("--",type(f))
print(f)
e = json.loads(f)
print(type(e))
print(e)
print(e['a'])


data={"code":10000,"data":0}
print(type(data))
print(data )
data={'code':10000,'data':0}
print(type(data))
print(data )
data= json.dumps(data)
data = json.loads(data)
print(type(data))
print(data['data'])

