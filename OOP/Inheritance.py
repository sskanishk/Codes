class Animal:
    cool = True

    def make_sound(self, sound):
        return f"this animal says {sound}"
class Cat(Animal):
    pass

class Dog:
    pass


# a = Animal()
# print(a.make_sound('CHRIP'))

b = Cat()
print(b.make_sound("MEOW"))
print(b.cool)
print(Animal.cool)

# b is object/instance of Cat and Animal as well
print(isinstance(b, Cat))
print(isinstance(b, Animal))
print(isinstance(b, object))

# d is object/instance of Dog but not other class
d = Dog()
print(isinstance(d, Cat))
print(isinstance(d, Animal))
print(isinstance(d, object))
#