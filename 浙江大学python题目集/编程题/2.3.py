n = int(input())
cost = 0.0
if n < 0:
    print("Invalid Value!")
elif n <= 50:
    cost = 0.53 * n
    print(f'cost = {cost:.2f}')
else:
    cost = 26.5 + (n - 50) * 0.58
    print(f'cost = {cost:.2f}')
