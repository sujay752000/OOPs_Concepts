""" Class : .is a blueprint for objects or instance
            .is a collection of objects or instances
            .has its own attributes and methods(behaviour)
    
    Object : is instance of a class, and 
            .has its own data
            .can access methods of class
            .its own identiity (stored own its unique memory address) also can provide name for each object

    Object Instantiation: creating object or instance is called object instantiation
                          during, object instantiation Constructor is invoked

"""
class Student:  # class ClassName

    college = "College of Engineering Chengannur"   # class attribute

    def __init__(self, rollno, name):
        self.student_roll = rollno            # instance attribute
        self.student_name = name              # instance attribute
        print("Constructor is invoked")



Student_1 = Student(55, "Sujay Prasad")
print(Student_1.college, Student_1.student_roll, Student_1.student_name)

