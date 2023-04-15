class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add Another Cat


class Mishu(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
Cat1 = Mishu("Mishu", 2)
Cat2 = Sally("Sally", 4)
Cat3 = Simon("Simon", 4)

my_cats = [Cat1, Cat2, Cat3]

# 3 Use a for loop to make all the cats walk
for char in my_cats:
    print(char.walk())
