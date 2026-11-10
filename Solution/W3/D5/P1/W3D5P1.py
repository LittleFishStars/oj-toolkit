def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


ops = {"add": add, "sub": sub, "mul": mul, "div": div}

m = int(input())
for _ in range(m):
    op, a, b = input().split()
    a, b = int(a), int(b)
    result = ops[op](a, b)
    if op == "div":
        print(f"{result:.2f}")
    else:
        print(result)
