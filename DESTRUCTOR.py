""" 
Destructors are called when an object gets destroyed. 
In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically. 
The __del__() method is a known as a destructor method in Python.
It is called when all references to the object have been deleted i.e when an object is garbage collected.
"""

class Student:

    def __init__(self, name, age, total_marks, grade):
        print(f"Constructor invoked - creating object {self} and initializing attributes")
        self.name = name
        self.age = age
        self.total_marks = total_marks
        self.grade = grade

    # destructor to remove / delete object from memory
    def __del__(self):     # just customized to show how internally __del__() works on calling del obj 
        print(f"Destructor invoked - removing object {self} from memory")


    
    def __delattr__(self, attr):    # just customized to show how internally __delattr__() works on calliung del obj.attr_name
        print(f"Deleting Attribute {attr}")
        super().__delattr__(attr)


    
    def print_details(self):    
        print(f"\n\tName = {self.name}\n\tAge = {self.age}\n\tTotal Marks = {self.total_marks}\n\tGrade = {self.grade}\n\n")




stu_1 = Student("Sujay Prasad", 24, 81.7, "A")

stu_1.print_details()

####################### Deleting Attributes of Object - deleting total_marks attribute og object stu_1: #########################
# 1. using del obj.attr_name : which internally calls the __delattr__()
# del stu_1.total_marks

# 2. or using direct call __del__(attribute_name)
stu_1.__delattr__("total_marks")


# stu_1.print_details() - shows attribute error because we removed total_marks attribute earlier




################################################# Deleting Object stu_1: #######################################################
# python's garbage collector automatically calls the destructor __del__() at programs end - to free the resource

# also if needed then we can call destructor using
# 1. del obj - which internally calls the __del__() method : right way

del stu_1
# 2. or directly call - obj.__del__() : leads to invoke object twice
