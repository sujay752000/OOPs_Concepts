""" 
Inheritence : Inheritance allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class). This promotes code reuse, modularity, and a hierarchical class structure.

Method Overrriding :

            Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. When a method in a subclass has the same name, the same parameters or signature, and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

            The version of a method that is executed will be determined by the object that is used to invoke it. If an object of a parent class is used to invoke the method, then the version in the parent class will be executed, but if an object of the subclass is used to invoke the method, then the version in the child class will be executed. In other words, it is the type of the object being referred to (not the type of the reference variable) that determines which version of an overridden method will be executed.



Single Inheritance: A child class inherits from one parent class.

 
"""


class Parent:   # Parent Class

    p_family_name = "Kannankara"

    def __init__(self, name, age):
        self.p_name = name
        self.p_age = age


    def display_complete_details(self):
        print(f"\n\tParent Name = {self.p_name}")
        print(f"\tParent Age = {self.p_age}")


class Child(Parent):    # Child Class

    c_family_name = "Vyshnavam"

    def __init__(self, p_name, p_age, c_name, c_age):
        super().__init__(name=p_name, age=p_age)
        self.c_name = c_name
        self.c_age = c_age

    
    def display_child_details(self):
        print(f"\tChild Name = {self.c_name}")
        print(f"\tChild Age = {self.c_age}\n")



    def display_complete_details(self):         # method overriding : overriding display_complete_details()
        super().display_complete_details()      # calls the parent's display_complete_details() method
        self.display_child_details()



c1 = Child("Prasad", 55, "Sujay", 24)

print(c1.c_family_name)
print(c1.p_family_name)
c1.display_complete_details()
c1.display_child_details()
    