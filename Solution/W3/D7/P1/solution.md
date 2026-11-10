Python
```python
def to_postfix(expr):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []
    stack = []
    num = ""
    for ch in expr:
        if ch.isdigit():
            num += ch
            continue
        if num:
            output.append(num)
            num = ""
        if ch in prec:
            while stack and stack[-1] != "(" and prec[stack[-1]] >= prec[ch]:
                output.append(stack.pop())
            stack.append(ch)
        elif ch == "(":
            stack.append(ch)
        else:
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
    if num:
        output.append(num)
    while stack:
        output.append(stack.pop())
    return output


def evaluate(postfix):
    prec = {"+", "-", "*", "/"}
    values = []
    for token in postfix:
        if token not in prec:
            values.append(int(token))
        else:
            b = values.pop()
            a = values.pop()
            if token == "+":
                values.append(a + b)
            elif token == "-":
                values.append(a - b)
            elif token == "*":
                values.append(a * b)
            else:
                values.append(a // b)
    return values[-1]


expr = input()
print(evaluate(to_postfix(expr)))
```
