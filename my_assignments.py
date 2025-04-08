# 1. Print your name on the screen
print("My name is Efe")

# 2. Create a variable and assign a value (string or number)
name = "Efe"
age = 20

# 3. Display the type of the variable
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>

# 4. Write an if statement (check if number is bigger than something)
x = 10
if x > 5:
    print("x is greater than 5")

# 5. Create a list (fruits, cars, students...)
fruits = ["apple", "banana", "orange"]

# 6. Display each element of the list using a for loop
for fruit in fruits:
    print(fruit)

# 7. Create a dictionary (student, car, animal...)
student = {
    "name": "Efe",
    "age": 20,
    "class": "12A"
}

print(student["name"])  # Output: Efe

# 8. Create a class (Student, Animal...)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create an object from the class
student1 = Student("Efe", 20)
student1.show_info()
