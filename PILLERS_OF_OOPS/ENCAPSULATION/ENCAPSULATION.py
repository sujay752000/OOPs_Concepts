"""
Encapsulation : Wrapping up of data (attributes), methods into a single unit , typically a class is known as encapsulation

* Encapsulation is the process of hiding the internal state of an object and all interactions like accessing, modifying operations can be performed with the respective object  of class

"""


"""
How Encapsulation Works :
        * Data Hiding: The variables (attributes) are kept private or protected, meaning they are not accessible directly from outside the class. Instead, they can only be accessed or modified through the methods.

        * Access through Methods: Methods act as the interface through which external code interacts with the data stored in the variables. For instance, getters and setters are common methods used to retrieve and update the value of a private variable.

        * Control and Security: By encapsulating the variables and only allowing their manipulation via methods, the class can enforce rules on how the variables are accessed or modified, thus maintaining control and security over the data.

"""


"""

Access Modifiers : Public , Protected and Private

    Public : By default, all members in Python are public.

             Public members can be accessed freely both inside and outside the class.


    Protected : Denoted by a single underscore _ before the member name.

                These members are meant to be accessed only within the class and its subclasses, though technically they are still accessible outside the class.


    Private : Denoted by a double underscore __ before the member name.

              These members cannot be accessed directly outside the class, providing true data hiding.

              Python uses name mangling to make private members less accessible by changing their names internally.

"""

"""
Name Mangling : is a technique that is used to convert names of (attributes / methods) classified as private or protected , internally so that it can't be accessed outside the class

for protedcted members : _ (underscore) name (attributes / methods)

                        eg "_rollno"


for private members : _ ClassName __name(attributes / methods)

                        eg "_ClassNmae__rollno"


for public members : "name(attributes / methods)"

                        eg "rollno"

"""


class Person:
    def __init__(self, name, addr, mobile_no, aadhar_no):

        # public attributes
        self.name = name
        self.addr = addr

        # protectted attribute
        self._mobile_no = mobile_no

        #  private attribute
        self.__aadhar_no = aadhar_no



    # public method
    def basic_details(self):
        print(f"Basic details are : \n\tName = {self.name}\n\tAddress = {self.addr}\n")


    # Getter method  to get private attribute value (Aaadhar no) - public method 
    def get_aadhar_no(self):
        print(f"\nAaadhar no = {self.__aadhar_no}")
    

    # Setter method  to set / update private attribute value (Aaadhar no) - public method
    def set_aadhar_no(self, aadhar_no):
        self.__aadhar_no = aadhar_no
        print("\nAadhar updated successfully")
    

    # protected method
    def _personal_details(self):
        print(f"Personal details are : \n\tName = {self.name}\n\tAddress = {self.addr}\n\tMobile no : {self._mobile_no}\n\tAadhar no : {self.__aadhar_no}\n")


class Family(Person):

    def __init__(self, name, addr, mobile_no, aadhar_no, family_name, family_role):
        super().__init__(name=name, addr=addr, mobile_no=mobile_no, aadhar_no=aadhar_no)
        self._family_name = family_name     # protected attribute
        self._family_role = family_role     # protected attribute


    def family_details(self):
        print("Family details are : \n")
        print(f"\tFamily Name = {self._family_name}")
        print(f"\tFamily Role = {self._family_role}")


    def complete_details(self):
        print("\n\nComplete details are : \n")
        self._personal_details()
        self.family_details()


p1 = Family("Sujay", "Vyshnavam kandalloor", "9633734319", "3214 1297 9201", "Vyshnavam", "child")

p1.basic_details() # public method of Person Class

p1.family_details() # public method of Family Class

p1.complete_details()   # publc method of Family Class

p1.get_aadhar_no()  # public method to view private attribute (getter method)

p1.set_aadhar_no("4127 4562 9804") # public method to update / set private attribute (setter method)




""" Accessing through : Name Mangling """

print(dir(p1))

# accessing private atribute : aadhar no using name mangling 
print(p1._Person__aadhar_no)

# accessing protected atribute : mobile no using name mangling 
print(p1._mobile_no)