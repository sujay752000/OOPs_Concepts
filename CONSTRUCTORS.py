# __new__ and __init
# The method __new__ is the constructor that creates a new instance of the class while __init__ is the initializer that sets up the instance’s attributes after creation. These methods work together to manage object creation and initialization.

class Student(object):

    # *args and ** kwargs are provided because __init__ (constructor) will call __new__ to create instance first then only instance is initialized,
    # so, if we passing parameters to constructor (__init__ ) like positional, or cvollection(list, tuple ..), we need to handle with *args and **kwargs
    def __new__(cls, *args, **kwargs):  # cls = reference parameter of Student class itself 
        print("Object / instance is created")
        instance =  super().__new__(cls)    # returns instance / object from super class i,e by default object class, by accessing super class's __new__ method
        return instance
    

    def __init__(self, name, roll, total_marks):
        print("Object / instance is initialized\n\n")
        self.name = name
        self.roll = roll
        self.total_marks = total_marks

stu_1 = Student("Sujay Prasad", 55, 81.7)   # object instantiation i,e object creation + initialisation




# Types of Constructors 
#       1. Default Constructor
#       2. Parameterized Constructor




# 1. Default Constructor
#           A default constructor does not take any parameters other than self. It initializes the object with default attribute values.
# eg

class College:

    def __init__(self):     # default Constructor
        print("I am default Constructor")
        self.college_name = "CEC"
        self.principal = "Sujay Prasad"

    def print_details(self):
        print(f"College name = {self.college_name}\nPrincipal  name = {self.principal}\n\n")


c1 = College()
c1.print_details()





# 2. Parameterized Constructor
#           A parameterized constructor accepts arguments to initialize the object’s attributes with specific values.

class Home:

    def __init__(self, father, mother, brother, me):    # parameterized constructor
        print("I ma Parameterized Constructor")
        self.father = father
        self.mother = mother
        self.brother = brother
        self.me = me

    def print_details(self):
        print(f"father = {self.father}\nMother = {self.mother}\nBrother = {self.brother}\nMe  = {self.me}\n\n")


h1 = Home("S prasad", "Sreedevi R", "Suraj Prasad", "Sujay Prasad")
h1.print_details()

