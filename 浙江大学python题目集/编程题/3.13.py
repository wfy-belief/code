# 凯撒密码
# 明文 ord
s1 = [chr(i + 65) for i in range(26)]
# 密文
s2 = reversed(s1)
rex = dict(zip(s1, s2))

s = input()
ans = map(lambda x: rex[x] if x.isupper() else x, s)
print(*ans, sep='')
