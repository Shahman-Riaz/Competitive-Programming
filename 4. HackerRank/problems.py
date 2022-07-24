class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

print(f'{a.name}&{b.name} ({a.capacity.__add__(b.capacity)}L)')