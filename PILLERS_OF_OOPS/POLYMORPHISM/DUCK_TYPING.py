"""
Duck Typing : Python is known for its “duck typing” philosophy, which is a form of polymorphism where the type or class of an object is less important than the methods it defines. When you use an object's method without knowing its type, as long as the object supports the method invocation, Python will run it. This is often summarized as “If it looks like a duck and quacks like a duck, it must be a duck.”
"""

class Duck:

    def can_swim(self):
        print("I am Duck and i can swim")

    def can_speak(self):
        print("I am Duck and i Quak !!")



class Dog:

    def can_swim(self):
        print("I am Dog and i can swim")

    def can_speak(self):
        print("I am Dog and i Bark !!")



def call_methods(obj):
    # basically the methods determines the type of objects
    obj.can_swim()
    obj.can_speak()


lst_objects = [Duck(), Dog()]

for obj in lst_objects:
    call_methods(obj)

    