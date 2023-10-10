class complex_number:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def __add__(self,other):
        return complex_number(self.real+other.real,self.image+other.image)
    def __sub__(self,other):
        return complex_number(self.real+other.real,self.image+other.image)
    def __multi__(self,other):
        return complex_number((self.real+other.real)-(self.image+other.image),(self.real+other.real)+(self.image+other.image))
    def __str__(self):
        if self.image<0:
            return f"{self.real}-{self.image}"
        else:
            return f"{self.real}+{self.image}"
real1=float(input("Enter the real part of the first complex number"))
image1=float(input("Enter the imaginary part of the first complex number"))
real2=float(input("Enter the real part of the second complex number"))
image2=float(input("Enter the imaginary part of the second complex number"))
complex_num1=complex_number(real1,image1)
complex_num2=complex_number(real2,image2)
add_result=complex_num1+complex_num2
sub_result=complex_num1-complex_num2
multi_result=complex_num1*complex_num2
print("First complex number:",complex_num1)
print("Second complex number:",complex_num2)
print("Addition result:",add_resut)
print("Subtraction result:",sub_resut)
print("Multiplication result:",multi_resut)