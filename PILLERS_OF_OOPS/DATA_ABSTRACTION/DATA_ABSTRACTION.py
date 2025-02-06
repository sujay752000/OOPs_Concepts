"""
Data Abstraction : Data abstraction is one of the most essential concepts of Python OOPs which is used to hide irrelevant details from the user and show the details that are relevant to the users

It enables programmers to hide complex implementation details while just showing users the most crucial data and functions.

In Python, abstraction can be achieved using abstract classes and interfaces provided by the abc (Abstract Base Class) module.

"""

"""
Implementation of Data Abstraction in Python

1. Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class. If we do not implement the abstract methods of base class in the child class then our code will give error.

Example Using Abstract Classes
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def vehicle_emission_standard(self):    # Concrete method : not need to override in sub classes
        print("BS6 -  Bharat Stage 6")

    @abstractmethod                         # abstract method  : need to implement in all sub classes
    def start_vehicle(self):
        pass

    @abstractmethod
    def stop_vehicle(self):
        pass

    def accelerate(self):
        pass

    def change_gear(self):
        pass



class Car(Vehicle):

    def __init__(self, car_name, car_engine_type, car_brakes, car_top_speed, car_total_gear):
        self.car_name = car_name
        self.car_engine_type = car_engine_type
        self.car_brakes = car_brakes
        self.car_top_speed = car_top_speed
        self.car_total_gear = car_total_gear


    def start_vehicle(self):
        print(f"Starting Engine {self.car_engine_type}")
        print(f"{self.car_name} started ... wroom wroom..")


    def stop_vehicle(self):
        print(f"Applying {self.car_brakes} braking ....")
        print(f"{self.car_name} stopped ..")


    def accelerate(self, speed):
        if speed <= self.car_top_speed:
            print(f"{self.car_name} crusing at {speed} km/hr")
        else:
            print(f"{self.car_name} can go max upto {self.car_top_speed} km/hr")


    def change_gear(self, gear):
        if gear <= self.car_total_gear:
            print(f"{self.car_name} changed gear to .. {gear}")
        else:
            print(f"{self.car_name} only have {self.car_total_gear} gears")

        

car_obj = Car("Porsche 911", "v12", "brembo", 240, 7)

car_obj.vehicle_emission_standard()
car_obj.start_vehicle()
car_obj.accelerate(100)
car_obj.change_gear(7)
car_obj.stop_vehicle()



"""
2. Interface in Python
Python does not have a built-in interface keyword, but we can create interfaces using abstract classes with only abstract methods.

Interface : is a pure Abstract Class , menaing no concrete method , must contain only abstract methods

Example of Interface
"""

class Animal(ABC):
    """Interface : Class containing only abstract methods """

    @abstractmethod
    def animal_life_span(self):
        pass

    @abstractmethod
    def animal_type(self):
        pass


class Lion(Animal):

    def animal_life_span(self):
        print("Life Span of Lion : 20 yrs")


    def animal_type(self):
        print("Lion Belongs to Carnivorous")


l1 = Lion()
l1.animal_life_span()
l1.animal_type()