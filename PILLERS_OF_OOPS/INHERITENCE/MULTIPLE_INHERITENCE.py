""" 
Multiple Inheritence : a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.


Method Resolution Order : In Python, every class whether built-in or user-defined is derived from the object class and all the objects are instances of the class object. Hence, the object class is the base class for all the other classes.
In the case of multiple inheritance, a given attribute is first searched in the current class if it’s not found then it's searched in the parent classes. The parent classes are searched in a left-right fashion and each class is searched once.
"""


class Father:

    def __init__(self, name, height, weight, *args, **kwargs):
        print("__init__ of Father is excuting")
        super().__init__(*args, **kwargs) # calls the next class in mro i,e Mother
        self.f_name = name
        self.f_height = height
        self.f_weight = weight


    def father_details(self):
        print(f"\n\tFather Name = {self.f_name}")
        print(f"\tFather Height = {self.f_height} cm ")
        print(f"\tFather Weight = {self.f_weight} kg ")




class Mother:

    def __init__(self, name, height, weight, *args, **kwargs):
        print("__init__ of Mother is excuting")
        super().__init__(*args, **kwargs)   # calls the next class in mro i,e Hereditory
        self.m_name = name
        self.m_height = height
        self.m_weight = weight

    def mother_details(self):
        print(f"\n\tMother Name = {self.m_name}")
        print(f"\tMother Height = {self.m_height} cm ")
        print(f"\tMother Weight = {self.m_weight} kg ")




class Hereditory:

    def __init__(self, *args, **kwargs):
        print("__init__ of Hereditory is excuting") # calls the next class in mro i,e object
        super().__init__(*args, **kwargs)

    skin_tone = "wheatish"
    religion = "Hindu"
    sub_caste = "Nair"





class Child(Father, Mother, Hereditory):        # mro order -> Father -> Mother -> Hereditory -> object

    def __init__(self, f_name, f_height, f_weight, m_name, m_height, m_weight, c_name):

        # we need call call each Class's __init__() to initialize attributes  i,e
        # Father.__init__(self, name=f_name, height=f_height, weight=f_weight)
        # Mother.__init__(self, name=m_name, height=m_height, weight=m_weight) 

        # or

        super().__init__(f_name, f_height, f_weight, m_name, m_height, m_weight)    # in this way only one time needs to call __init__() to initialize all the class attributes
        self.c_name = c_name


    @property
    def c_height(self):
        child_height = (self.f_height + self.m_height) // 2
        return child_height


    @property
    def c_weight(self):
        child_weight = (self.f_weight + self.m_weight) // 2
        return child_weight


    def child_details(self):
        print(f"\n\tChild Name = {self.c_name}")
        print(f"\tChild Height = {self.c_height} cm ")
        print(f"\tChild Skin Tone = {self.skin_tone} ")
        print(f"\tChild Religion = {self.religion} ")
        print(f"\tChild Sub Caste = {self.sub_caste} \n")



c1 = Child("S prasad", 182, 80, "Sreedevi R", 172, 60, "Sujay Prasad")

print(f"Method Resolution Order for class Child : \n\t{Child.mro()}")  # Method Resolution Order

c1.child_details()


c1.father_details()

c1.mother_details()