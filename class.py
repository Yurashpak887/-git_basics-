class Car:
    def __init__(self, mark, model, year, owner):
        self.mark = mark
        self.model = model
        self.year = year
        self.owner = owner

    def __repr__(self):
        return f'{self.mark},{self.model}, {self.year}, {self.owner}'

class WithOwner(Car):
    def change_owner(self, new_owner):
        self.owner = new_owner


a = Car("Tesla", "S", "2020", "Yura")
print(a.__repr__())
a1 = WithOwner("Tesla", "X", "2022", "Yura")
print(a1.__repr__())
a1.change_owner("Baky")
print(a1.__repr__())
