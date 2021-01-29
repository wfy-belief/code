import re

# 16进制 0-9 A-F a-f
s = input()
ans = re.sub(r'[^0-9a-fA-F]', '', s)
if not ans:
    ans = '0'
int_ans = int(ans, 16)
if -1 < s.find('-') < s.find(ans[0]):
    int_ans = -int_ans
print(int_ans)
