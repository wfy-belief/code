n = int(input())
ans = 0
for _ in range(n):
    s = input()
    # 如果存在字母
    if not s[:17].isdigit():
        ans = 1
        print(s)
        continue
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ans_add = sum([int(key) * value for key, value in zip(s[:17], weight)])
    transform = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    # 判断合法性
    transform_s = s[:17] + transform[ans_add % 11]

    if transform_s != s:
        ans = 1
        print(s)
if not ans:
    print('All passed')
