n = int(input())
count = 0
for i in range(0, n):
    for j in range(0, n - i):
        a = chr(ord("A") + count)
        count = count + 1
        print("%s " % a, end="")
    print()
