s = input()
ans = []
for x in s:
    if x.isupper() and x not in ans:
        ans.append(x)
print(''.join(ans) if ans else 'Not Found')
