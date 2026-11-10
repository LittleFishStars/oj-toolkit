class Date:
    def __init__(self, m, d):
        self.total = (m - 1) * 30 + (d - 1)

    def __add__(self, k):
        result = Date(1, 1)
        result.total = (self.total + k) % 360
        return result

    def __str__(self):
        return f"{self.total // 30 + 1}/{self.total % 30 + 1}"


m, d, k = map(int, input().split())
print(Date(m, d) + k)
