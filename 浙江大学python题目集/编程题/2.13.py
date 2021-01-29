def get_money(x):
    if x <= 15:
        return 4 * x / 3
    return 2.5 * x - 17.5


n = int(input())
print(f'{get_money(n):.2f}')
