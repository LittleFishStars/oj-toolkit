a = set(input().split())
b = set(input().split())
common = a & b
if common:
    print(" ".join(sorted(common)))
else:
    print("None")
