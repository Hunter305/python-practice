
class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


sn = Dog("Berger", "BullDog")


print(sn.breed)

sn.breed = "Lab"

print(sn.breed)


class Animal():
    def __init__(self, animal_name):
        self.animal_name = animal_name


class Cat(Animal):
    def __init__(self, animal_name, name, breed):
        super().__init__(animal_name)
        self.name = name
        self.breed = breed


cat1 = Cat(animal_name="cat", name="peter", breed="persian")

print(cat1.animal_name)
