def get_index(ch):
    for index, value in enumerate(s[::-1]):
        if ch == value:
            print(f'{len(s) - index - 1} {value}')


s = input()
a, b = input().split()
get_index(b)
get_index(a)
