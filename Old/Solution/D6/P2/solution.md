C语言
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAXN 30

int stack[MAXN];
int top;

int main() {
    int n;
    scanf("%d", &n);
    top = 0;
    for (int i = 0; i < n; i++) {
        char token[20];
        scanf("%s", token);
        if (isdigit(token[0]) || (token[0] == '-' && token[1] != '\0')) {
            stack[top++] = atoi(token);
        } else {
            int b = stack[--top];
            int a = stack[--top];
            switch (token[0]) {
                case '+': stack[top++] = a + b; break;
                case '-': stack[top++] = a - b; break;
                case '*': stack[top++] = a * b; break;
                case '/': stack[top++] = a / b; break;
            }
        }
    }
    printf("%d\n", stack[0]);
    return 0;
}
```

Python
```python
n = int(input())
tokens = input().split()
stack = []
for token in tokens:
    if token in ("+", "-", "*", "/"):
        b = stack.pop()
        a = stack.pop()
        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            stack.append(a // b)
    else:
        stack.append(int(token))
print(stack[0])
```
