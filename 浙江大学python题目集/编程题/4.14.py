import sys

s = sys.stdin.read()
letter, digit, blank, other = 0, 0, 0, 0
for i in s[:-1]:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        blank += 1
    else:
        other += 1
print(f'letter = {letter}, blank = {blank}, digit = {digit}, other = {other}')
