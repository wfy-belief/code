s = input()
ans = list(filter(lambda x: x.isupper() and x not in ('A', 'E', 'I', 'O', 'U'), s))
print(len(ans))
