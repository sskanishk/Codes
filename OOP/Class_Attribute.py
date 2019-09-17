# A user class with 3 instance attribute but no instance method (aside from __init__)

class user:

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


print(user.active_user)
# user 1
user1 = user('Apple', 'Smith', 9)
# user 2
user2 = user('micro', 'dell', 4)

print(user.active_user)
# user 3
user2 = user('micro', 'dell', 4)

# user logout
print(user2.logout())

# final user is 2
print(user.active_user)



