class Vehicle:
    def __init__(self, brand, cost, __jadoo):
        self.brand = brand
        self.cost = cost
        self.__jadoo = __jadoo


double_underscore = Vehicle('use with class and parameter', 73278, 'jadoo dekho')

# this code will work
# __jadoo is converted into _Vehicle__jadoo
# name mangling put class name first
print(double_underscore.brand, double_underscore.cost, double_underscore._Vehicle__jadoo)

# this code wil have error
# we cannot use this __jadoo
print(double_underscore.brand, double_underscore.cost, double_underscore.__jadoo)
