Python
```python
class Card:
    order = {c: i for i, c in enumerate(
        ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])}

    def __init__(self, face):
        self.face = face

    def __lt__(self, other):
        return Card.order[self.face] < Card.order[other.face]

    def __str__(self):
        return self.face


cards = [Card(f) for f in input().split()]
cards.sort()
print(*cards)
```
