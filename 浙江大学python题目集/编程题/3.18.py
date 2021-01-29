ans = []
for s in input():
    if s.isalpha() and s.lower() not in ans and s.upper() not in ans:
        ans.append(s)
    if len(ans) == 10:
        print(''.join(ans))
        break
else:
    print('not found')
