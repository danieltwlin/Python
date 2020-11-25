import redis                              # 导入redis 模块
# 連線 redis server
r = redis.Redis(host='localhost', port=6379, decode_responses=True)


r.set('name', 'runoob')              # 设置 name 对应的值
print(r.get('name'))                   # 取出键 name 对应的值
# print( r['name'] )
print( type( r.get('name')) )          # 查看类型


# SADD,SPOP 

r.sadd("10",1,2,3,4,5,6)
print(r.smembers('10'))
r.spop('10')
print(r.smembers('10'))

# RPUSH, LPOP

r.rpush('guy','hello')
print(r.lrange('guy', 0,-1))
r.lpop('guy')
print(r.lrange('guy', 0,-1))


# hashlib

import uuid 
import hashlib

rand = uuid.uuid4().hex[:14]
id = hashlib.md5(rand.encode('utf-8')).hexdigest()

print(id)

