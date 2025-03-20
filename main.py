
from animal import Animal

# Creating instances
cat = Animal("Cat", "Mammals", 4, ["climbing", "jumping", "hunting"])
dog = Animal("Dog", "Mammals", 4, ["running", "swimming", "guarding"])
eagle = Animal("Eagle", "Birds", 2, ["flying", "hunting", "sharp vision"])
frog = Animal("Frog", "Amphibians", 4, ["jumping", "swimming", "croaking"])
snake = Animal("Snake", "Reptiles", 0, ["slithering", "hunting", "camouflage"])

# Store in a list
animals = [cat, dog, eagle, frog, snake]

# Print details
for animal in animals:
    print(animal.show_info())
