""" 
METHOD OVERRIDING - Run Time Polymorphism (Dynamic Binding): Method overriding is achieved through inheritance, which allows a subclass to provide a specific implementation of a method that is already defined in its parent class. The method in the child class should have the same name, same parameters, and same return type as the method in the parent class.

if we accessing the method through sub class object then method in sub class gets invoked .. similary if we are accessing the method with parent class object the, parent class method is invoked
"""

class Parent:

    def display(self):
        print("I am class Parent")


class Child(Parent):


    def display(self):
        print("I am class Child")


obj1 = Child()
obj1.display()

obj2 = Parent()
obj2.display()