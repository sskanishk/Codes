# A user class with 3 instance attribute but no instance method (aside from __init__)

class user:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


    # below is the instance method
    def full_name (self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 60

    def birthday(self):
        self.age += 1
        return f"happy {self.age}th, {self.first}"

    # this function will throw error, i doesn't have self in parameter
    def say_hi():
        print('hello!!')

user1 = user('Apple', 'Smith', 9)
user2 = user('micro', 'dell', 4)

# print(user1.full_name())
# print(user1.full_name())
# print(user1.likes("iphone"))

print(user1.birthday())
print(user2.is_senior())