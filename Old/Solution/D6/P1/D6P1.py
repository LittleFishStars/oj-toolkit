n = int(input())
stack = []
for _ in range(n):
    parts = input().split()
    op = int(parts[0])
    if op == 1:
        stack.append(int(parts[1]))
    elif op == 2:
        if stack:
            print(stack.pop())
        else:
            print("Empty")
    elif op == 3:
        if stack:
            print(stack[-1])
        else:
            print("Empty")
    elif op == 4:
        print(len(stack))
