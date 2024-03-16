class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


sn = Dog("Berger", "BullDog")


print(sn.breed)

sn.breed = "Lab"

print(sn.breed)
