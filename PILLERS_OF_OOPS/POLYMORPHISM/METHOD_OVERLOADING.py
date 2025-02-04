"""
METHOD OVERLOADING - Compile time polymorphism (static binding) : Unlike some other languages like Java, Python does not support method overloading directly (having multiple methods with the same name but different parameters). However, it can be achieved using default arguments, *args and **kwargs.

Unlike statically typed languages like Java and C++, Python does not support method overloading in the traditional sense. In those languages, you can define multiple methods with the same name but different parameter lists, and the compiler decides which method to call based on the number and types of arguments (static binding).

However, Python is dynamically typed, meaning:

No Type Declarations: Python functions do not require explicit type declarations, so the interpreter cannot distinguish overloaded methods based on parameter types.

Single Method Definition: In Python, if you define multiple methods with the same name in a class, the last definition overwrites the previous ones.

Flexible Function Parameters: Python allows default arguments, *args, and **kwargs, which provide a more flexible way to achieve similar behavior.
"""


def add(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)


add(1, 2)

add(1, 2, 3, 4)