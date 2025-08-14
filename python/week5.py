from abc import ABC, abstractmethod

class Vehichle(ABC):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    @abstractmethod
    def start():
        pass
    
    @abstractmethod
    def stop():
        pass
    
    def __str__(self):
        return f"brand={self.brand}, color={self.color}"
        

class Matatu(Vehichle):
    def __init__(self, brand, color, speed_limit):
        super().__init__(brand, color)
        self.speed_limit = speed_limit
        
    def __str__(self):
        return f"{super().__str__()}, speed_limit={self.speed_limit}"
    
    def start(self):
        print("Matatu has been started")
    
    def stop(self):
        print("Matatu has been stopped")
        
class Car(Vehichle):
    def __init__(self, brand, color, price):
        super().__init__(brand, color)
        self.__price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Car price cannot be zero or less")
        else:
            self.__price = value
    
    def start(self):
        print("Car has been started")
        
        
    def stop(self):
        print("Car has been stopped")
        
    
mat = Matatu(brand="Toyota", color="Yellow", speed_limit=180);
car = Car(brand="Nissan", color="blue", price=1_000_000)

print(f"Matatu: {mat}")
print(f"Car: {car}")

object_array = [mat, car]

def move(object_array):
    for object in object_array:
        object.start()
        object.stop()
        
move(object_array)