"""
Hierarchical Inheritence : A derived class is inheriting from multiple Parent classes
"""
class Father:

    family_name = "Vyshnavam"

    def __init__(self, name, height, weight):
        self.f_name = name
        self.f_height = height
        self.f_weight = weight


    def father_details(self):
        print(f"\n\tFather Name = {self.f_name}")
        print(f"\tFather Height = {self.f_height} cm ")
        print(f"\tFather Weight = {self.f_weight} kg ")


class ElderSon(Father):

    def __init__(self, fname, fheight, fweight, elname):
        super().__init__(name=fname, height=fheight, weight=fweight)
        self.el_son_name = elname
        self.el_son_height = self.f_height
        self.el_son_weight = self.f_weight

    
    def elderson_details(self):
        print(f"\n\tElder Son Name = {self.el_son_name}")
        print(f"\tElder Son Height = {self.el_son_height} cm ")
        print(f"\tElder Son Weight = {self.el_son_weight} kg ")
        print(f"\tElder Son Family Name = {self.family_name} ")



class SmallerSon(Father):

    def __init__(self, fname, fheight, fweight, smname):
        super().__init__(name=fname, height=fheight, weight=fweight)
        self.sm_son_name = smname
        self.sm_son_height = self.f_height
        self.sm_son_weight = self.f_weight


    def smallerson_details(self):
        print(f"\n\tSmaller Son Name = {self.sm_son_name}")
        print(f"\tSmaller Son Height = {self.sm_son_height} cm ")
        print(f"\tSmaller Son Weight = {self.sm_son_weight} kg ")
        print(f"\tSmaller Son Family Name = {self.family_name} ")



# elder son object
el_son = ElderSon("S prasad", 182, 80, "Suraj Prasad")
el_son.elderson_details()
el_son.father_details()


# smaller son object
sm_son = SmallerSon("S prasad", 182, 80, "Sujay Prasad")
sm_son.smallerson_details()
sm_son.father_details()