class Vehicle:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost


# creating instance of Car,userx is a object
car = Vehicle("KIA", 5600000)
ship = Vehicle("Black Pearl", 78000000)

# this will give the address of object
print(car)

# this will show car is the object of class vehicle
print(type(car))

# this will print the paramenter passed in the car object
print(car.brand, car.cost)
print(ship.brand, ship.cost)