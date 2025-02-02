"""
Multilevel Inheritence : Multilevel Inheritance in Python is a type of Inheritance in which a class inherits from a class, which itself inherits from another class. It allows a class to inherit properties and methods from multiple parent classes, forming a hierarchy similar to a family tree.

"""

class GrandFather:

    def __init__(self, name, height, weight):
        self.gf_name = name
        self.gf_height = height
        self.gf_weight = weight


    def grandfather_details(self):
        print(f"\n\tGrand Father Name = {self.gf_name}")
        print(f"\tGrand Father Height = {self.gf_height} cm ")
        print(f"\tGrand Father Weight = {self.gf_weight} kg ")



class Father(GrandFather):

    def __init__(self, gfname, gfheight, gfweight, name, height, weight):
        super().__init__(name=gfname, height=gfheight, weight=gfweight)
        self.f_name = name
        self.f_height = height
        self.f_weight = weight


    def father_details(self):
        print(f"\n\tFather Name = {self.f_name}")
        print(f"\tFather Height = {self.f_height} cm ")
        print(f"\tFather Weight = {self.f_weight} kg ")



class Child(Father):

    def __init__(self, gfname, gfheight, gfweight, fname, fheight, fweight, cname):
        super().__init__(gfname=gfname, gfheight=gfheight, gfweight=gfweight, name=fname, height=fheight, weight=fweight)
        self.c_name = cname

    @property
    def c_height(self):
        height = (self.gf_height + self.f_height) / 2
        return height
    
    @property
    def c_weight(self):
        weight = (self.gf_weight + self.f_weight) / 2
        return weight
    

    def child_details(self):
        print(f"\n\tChild Name = {self.c_name}")
        print(f"\tChild Height = {self.c_height} cm ")
        print(f"\tChild Weight = {self.c_weight} kg ")



c1 = Child("Sreedharan Nair", 180, 75, "S Prasad", 184, 85, "Sujay Prasad")

print(Child.mro())

c1.child_details()

c1.father_details()

c1.grandfather_details()
