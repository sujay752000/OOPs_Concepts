"""
Polymorphishm : Polymorphism is a foundational concept in programming that allows entities like functions, methods and operators to behave differently based on the type of data they are handling.

poly : means many

morph : means forms

meaning : ability of functions, method and operators to behave in many different forms based on the data they are handling
"""

"""
Types of Polymorphism in Python

    1. Method Overriding (Runtime Polymorphism)

    2. Method Overloading (Compile-time Polymorphism) : not possible due to dynamic typing

    3. Operator Overloading

    4. Duck Typing
    
"""

# Implicit Polymorphism : already exist in default by python

# eg : + operator
print(1 + 2)      # adds numbers, when integer is passed
print("1" + "2")  # concatinate strings, when strings is passed


# eg : len()
print(len("sujay"))             # count total characters, when string is passed
print(len(["sujay", "prasad"])) # count total items, when list is passed