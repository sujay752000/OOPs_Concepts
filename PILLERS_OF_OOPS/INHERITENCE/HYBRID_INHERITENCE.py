""" 
Hybrid Inheritence : Combination of two or types of Inheritence
eg showing combination of : Multilevel + Multiple

A       
|
B       Z
|       |
----C----

"""


class Z:

    def show_Z(self):
        print("I am class Z")



class A:

    def show_A(self):
        print("I am class A")


class B(A):

    def show_B(self):
        print("I am class B")



class C(B, Z):
    def show_C(self):
        print("I am class C")


c1 = C()
c1.show_C()
c1.show_B()
c1.show_Z()
