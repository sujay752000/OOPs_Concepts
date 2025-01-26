class Student:
    """_summary_ :class contains details of students
    """

    college = "College of Engineering Chengannur"

    def __init__(self, name, age, total_marks):
        self.name = name
        self.age = age
        self.total_marks = total_marks


    def add_Marks(self, new_marks):
        self.total_marks += new_marks


    def print_Detials(self):
        print(f"\n Details are : \n\t Name = {self.name} \n\t Age = {self. age} \n\t Total Marks = {self.total_marks}")


    
stu_1 = Student("Sujay Prasad", 24, 85)
stu_1.add_Marks(10)
stu_1.print_Detials()


# Object Introspection : details or infromation about objects

# dir(obj) : returns a list of attributes, methods, and dunder methods belonging to an object
print(dir(stu_1))
#or  print(stu_1.__dir__())

# obj.__dict__ : return a dictionary of instance attribute : value
print(stu_1.__dict__)


# help(obj) : returns a string of  details according to the passed parameter like class, (instance or object)
print(help(int))