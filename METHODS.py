############################# METHODS
print("############################# METHODS")
class Student:
    def __init__(self, name):
        self.name = name

    # method always takes self as parameter
    def say_Hello(self):    # for an instance to call method we need to pass self, to represnt respective object/instance
        print(f"hello {self.name}")

    
s = Student("sujay prasad")
s.say_Hello()


############################# STATIC METHODS  - methods that don't take self as parameter , works at class level
print("\n############################# STATIC METHODS")

class Welcome:

    @staticmethod
    def goodmorning_Message():
        print("Good morning")


w1 = Welcome()
w1.goodmorning_Message()            # can be accessed by objects
Welcome.goodmorning_Message()       # ca be accessed by class



############################# CLASS METHODS - methods works at class level, the parameter represents the class itself

print("\n############################# CLASS METHODS")

class Details:

    college_name = "CEC - Chengannur"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_Details(self):
        print(f"Name = {self.name}\nAge = {self.age}\nCollege = {self.college_name}")


    @classmethod                # helps to make method as class method, by making the first parameter reference to class itself
    def change_College_Name(cls, new_college_name): # here cls reference to class
        cls.college_name = new_college_name


d1 = Details("sujay", 24)
d1.print_Details()

# changing class attribute of  respective instance to a new value ... only effects for this instance d2
d2 = Details("jiju", 24)
d2.college_name = "UIT Karuvatta"
d2.print_Details()

print(f"{Details.college_name}")    # Class Attribute not changed

Details.change_College_Name("Angels Arc")   # changing by class ... since it works at class level first parameter reprensts class itself

print(f"{Details.college_name}")   # class Attribute college_name changed to "Angels Arc"

d3 = Details("lijo", 24)
d3.change_College_Name("UIT Muthukulam")
d3.print_Details()
print(f"{Details.college_name}")   # class Attribute college_name changed to "UIT Muthukulam"

