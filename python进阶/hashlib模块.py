import hashlib

# 加密模块
'''
salt = b'wfy-belief'
md5 = hashlib.md5(salt)
md5.update(b'password')
# 输出
print(md5.hexdigest())
print(md5.digest())
'''
md5 = hashlib.md5(b'000131,000318,0722')
# 411322200008070619
# 541807220143
md5.update(b'541807220143')
# 54b22fa43f5bbc10e52e45358c991314
# 25bca90a47acb11e6f85e7d4462b9db1
print(md5.hexdigest())
# Ldm%2FMhJ%2F3DVAG5ZR3syS2Q%3D%3D
# Ldm%2FMhJ%2F3DVAG5ZR3syS2Q%3D%3D