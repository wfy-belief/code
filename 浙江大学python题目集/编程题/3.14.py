def transform(x):
    if x.isupper():
        return x.lower()
    if x.islower():
        return x.upper()
    return x


s = input()
ans = map(lambda x: transform(x), s[:-1])
print(*ans, sep='')
