text = input()

upper = 0
lower = 0
digit = 0
other = 0
for ch in text:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        other += 1

print(upper, lower, digit, other)
