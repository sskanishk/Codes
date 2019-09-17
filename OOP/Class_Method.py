class user:

    @classmethod
    def display_active_user(cls):
        return f"there are currently active users {cls.active_user}"

    @classmethod
    def rom_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)

    # class attribute
    active_user = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        user.active_user += 1


    # below is the instance method
    def logout(self):
        user.active_user -= 1
        return f"{self.first} logged out"

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
    # def say_hi():
    #     print('hello!!')

"""
print(user.active_user)
# user 1
user1 = user('Apple', 'Smith', 9)
# user 2
user2 = user('micro', 'dell', 4)

# technically wrong
# print(user1.display_active_user())
# class method it doest rely on any praticlar instance
print(user.display_active_user())

"""

user.from_string


