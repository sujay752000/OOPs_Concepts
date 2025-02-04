"""
OPERATOR OVERLOADING : Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because + operator is overloaded by int class and str class.

Python does not allow creating entirely new operators. However, Python provides operator overloading

eg : + operator

print(1 + 2)      # adds numbers, when integer is passed
print("1" + "2")  # concatinate strings, when strings is passed

"""

# there is no method to perform basic +, -, *, / calculation for complex number
# eg of Complex num : 6i + 3j

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def print_complex_number(self):
        print(f"{self.real}i + {self.imag}j")

    # Binary Operators Overloading
    def __add__(num1, num2):
        real = num1.real + num2.real
        imag = num2.imag + num2.imag
        return f"{real}i + {imag}j"
    
    def __sub__(num1, num2):
        real = num1.real - num2.real
        imag = num1.imag - num2.imag
        return f"{real}i + {imag}j"
    
    def __mul__(num1, num2):
        real = num1.real * num2.real
        imag = num1.imag * num2.imag
        return f"{real}i + {imag}j"
    
    def __truediv__(num1, num2):
        real = num1.real / num2.real
        imag = num1.imag / num2.imag
        return f"{real}i + {imag}j"
    



print("First Number")
complex_num1 = ComplexNumber(12, 6)
complex_num1.print_complex_number()


print("\n\nSecond Number")
complex_num2 = ComplexNumber(6, 3)
complex_num2.print_complex_number()


print("\n\nComplex Number Addition")
print(complex_num1 + complex_num2)

print("\n\nComplex Number Subtraction")
print(complex_num1 - complex_num2)

print("\n\nComplex Number Multiplication")
print(complex_num1 * complex_num2)

print("\n\nComplex Number Division")
print(complex_num1 / complex_num2)



"""
Binary Operators:
Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)


Comparison Operators:
Operator	Magic Method
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)


Assignment Operators:
Operator	Magic Method
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)


Unary Operators:

Operator	Magic Method
-	__neg__(self)
+	__pos__(self)
~	__invert__(self)

"""