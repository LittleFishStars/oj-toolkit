apples = list(map(int, input().split()))
hand = int(input())
reach = hand + 30
print(sum(1 for a in apples if a <= reach))
