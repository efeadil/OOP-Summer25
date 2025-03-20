# animal.py

class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def show_info(self):
        return f"{self.name} belongs to {self.group}, has {self.number_of_legs} legs, and can {', '.join(self.skills)}."


# Creating instances
animals = [
    Animal("Cat", "Mammals", 4, ["climbing", "jumping", "hunting"]),
    Animal("Dog", "Mammals", 4, ["running", "swimming", "guarding"]),
    Animal("Eagle", "Birds", 2, ["flying", "hunting", "sharp vision"]),
    Animal("Frog", "Amphibians", 4, ["jumping", "swimming", "croaking"]),
    Animal("Snake", "Reptiles", 0, ["slithering", "hunting", "camouflage"]),
]

# Print details
for animal in animals:
    print(animal.show_info())
