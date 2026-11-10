def digit_sum(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total


nums = list(map(int, input().split()))
result = sorted(nums, key=lambda x: (digit_sum(x), x))
print(*result)
