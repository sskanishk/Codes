class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # ticktick
    # # getter
    # def get_age(self):
    #     return self._age
    # # setter
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can not be negative")

    @property
    def full_name(self):
        return f"{self.first}  {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


# ticktcik
# jane = Human("Jane", "Lever", 567)
# print(jane.get_age())
# jane.set_age(78)
# print(jane.get_age())
# jane.set_age(-3)
# print(jane.get_age())

jane = Human('jane', 'Lever', 45)
print(jane.age)
# jane = Human('jane', 'Lever', -4)
# print(jane.age)
# work without paranethiese
# print(jane.age())
# jane.age = -4
# print(jane.age)
print(jane.full_name)
jane.full_name = "Rohit Ronkehede"
print(jane.full_name)

print(jane.__dict__)
# .