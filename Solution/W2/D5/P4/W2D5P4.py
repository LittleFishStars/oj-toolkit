n = int(input())

terms = [f"+x^{k}/{k}" if k % 2 else f"-x^{k}/{k}" for k in range(1, n + 1)]
print("".join(terms))
