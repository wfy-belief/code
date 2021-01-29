ch = input()
s = input()
index = s.rfind(ch)
print('Not Found' if index == -1 else f'index = {index}')
