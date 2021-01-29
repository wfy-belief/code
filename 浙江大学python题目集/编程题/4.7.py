n = int(input())
if n == 0:
    print("average = 0.0")
    print("count = 0")
else:
    l = list(map(int, input().split()))
    average = sum(l) / len(l)
    count_ = len([x for x in l if x >= 60])
    print(f'average = {average:.1f}')
    print(f'count = {count_}')
