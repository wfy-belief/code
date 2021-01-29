import re

s = input()
ans = re.findall(r'\d', s)
print(int(''.join(ans)))
