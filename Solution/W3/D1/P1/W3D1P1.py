def f(x):
    if x < 0:
        return -x
    if x < 10:
        return x * x
    return x + 100


x = int(input())
print(f(x))
