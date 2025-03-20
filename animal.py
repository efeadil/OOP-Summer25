class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def show_info(self):
        return f"{self.name} belongs to {self.group}, has {self.number_of_legs} legs, and can {', '.join(self.skills)}."
