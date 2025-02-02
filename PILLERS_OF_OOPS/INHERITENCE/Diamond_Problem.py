"""
Diamond Problem : It refers to an ambiguity that arises when two classes classB and ClassC inherit from a superclass ClassA and class ClassD inherits from both ClassB and ClassC. If there is a method “show()” which is an overridden method in one of ClassB and ClassC or both then the ambiguity arises which of the method “show()” ClassD should inherit.


Python uses MRO to resolve this problem : Method Resolution Order
MRO (Method Resolution Order) determines the sequence in which classes are searched when calling a method in multiple inheritance scenarios. Python uses the C3 Linearization (or C3 MRO) algorithm to establish this order.

MRO Algorithm - Step-by-Step
    1. Start from the Child Class
        Python first looks for the method in the child class itself.

    2. Left-to-Right Lookup in Parent Classes
        If not found, Python moves to the first parent (leftmost in the class declaration).

    3. Depth-First Search (But Maintains Order)
        It continues searching in a depth-first manner, but ensures that a parent is checked only after all its child classes have been checked.
        
    No Class is Visited Twice
    To prevent redundant method calls, a class appears only once in the MRO list.
"""


class A:

    def show(self):
        print("I am Class A")

    def display(self):
        print("I am Display at Class A")


class B(A):

    def show(self):
        print("I am Class B")


class C(A):

    def show(self):
        print("I am Class C")


class D(B, C):

    pass



obj = D()

# shows th MRO - Method Resolution Order
print(D.mro())      

"""
As per MRO :

    1. first check method from left -> to right class, i,e B -> C
        here, the class B contains show()
"""
obj.show() 



"""
As per MRO :

    1. first check method from left -> to right class, i,e B -> C
        here, the class B, C has no method

    2. then go for the first class in MRO (i,e class B): and check in depth wise seacch (Parent Wise)
        2.1 here, comes back to B
        2.2 and check its parent i,e class A
            class A contains method display() .. it gets executed

"""
obj.display()