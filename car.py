class Car:
    def __init__(self, brand, engine_type):
        self.brand = brand              
        self.__engine_type = engine_type  

    def display_engine_type(self):
        """Public method to access private attribute."""
        print(f"Engine type: {self.__engine_type}")

    def __start_the_engine(self):
        """Private method."""
        print(f"{self.brand}'s engine is starting... Vroom!")

    def start_the_car(self):
        """Public method to call private method."""
        self.__start_the_engine()


# Example usage:
if __name__ == "__main__":
    my_car = Car("Toyota", "Hybrid")
    print(f"Car brand: {my_car.brand}")       
    my_car.display_engine_type()             
    my_car.start_the_car()                    
   