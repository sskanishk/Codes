class Pet:
    allowed = ['dog', 'rabbit', 'rat', 'cat']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet! ")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet! ")
        self.species = species


dog = Pet('Snoofy', 'dog')
cat = Pet('sweety', 'cat')

# print(Pet.dog)
# print(Pet.cat)
# dog.species = 'Giraffe'

# set values of species with new one.
print(cat.species)
cat.set_species('rabbit')
print(cat.species)

# append elemnet in list
Pet.allowed.append('rohit')
print(cat.species)

# set the new value od species
cat.set_species('rohit')
print(cat.species)


print(cat)
print(cat.name)
print(dog)
print(dog.name)
print("Pet.allowed", Pet.allowed)
print("cat.allowed", cat.allowed)
print("dog.allowed",dog.allowed)
print("id - pet.allowed",id(Pet.allowed))
print("id - cat.allowed",id(cat.allowed))
print("id - dog.allowed",id(dog.allowed))
