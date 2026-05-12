#Finding the circumference and the Area by asking the user to input 
def Area():
    A=3.14*r*r
    C=2*3.14*r
    print(f"Area of the circle {A}")
    print(f"Circumference of the circle {C}")

r=float(input("Enter the value of the radius"))

Area()


#Program to calculate the interest 
def Interest():
    I=(P*T*R)/100
    print(f"The Interest is {I}")



P=float(input("Please enter the principal Amount"))
T=float(input("Please enter the tenure of your amount"))
R=float(input("Please enter the rate of interest"))

Interest()

# Function to find the hypotenuse 
import math 

def find_hypt(a,b):
    C=math.sqrt(a*a+b*b)
    print(f"The Hypotenuse of the triangle is {C}")

find_hypt(2,3)