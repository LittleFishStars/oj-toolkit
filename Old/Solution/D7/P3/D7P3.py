max_hours = 0
max_day = 0
for i in range(1, 8):
    school, extra = map(int, input().split())
    total = school + extra
    if total > max_hours:
        max_hours = total
        max_day = i
print(0 if max_hours <= 8 else max_day)
