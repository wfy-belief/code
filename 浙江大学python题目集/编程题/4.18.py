n = int(input())
num = [i for i in range(1, n + 1)]
if n == 1:
    print(n)
else:
    while len(num) >= 3:
        del num[2]  # 删除位置为2的数，然后后面会自动补充过来
        num.append(num.pop(0))  # 在把位置0弹出到队尾
        num.append(num.pop(0))  # 在把位置0弹出到队尾
    print(num[1])
