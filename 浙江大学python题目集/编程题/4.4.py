def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
for i in range(2, n // 2 + 1):
    if is_prime(i) and is_prime(n - i):
        print(f'{n} = {i} + {n - i}')
        break
