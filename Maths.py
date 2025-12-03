#Question # 1
# Area of a Rectangle:

length = float(input("Enter the length of the rectangle: "))  
width = float(input("Enter the width of rectangle: "))
area = length * width  
print(f"The area of a rectangle is {area}")

# Question # 2
#circumference of a circle:

radius = float(input("Enter the radius of the circle: ")) 
pi = 3.1459
circumference = 2*pi*radius
print(f"The circumference of the circle is{circumference}")

# Question # 3
#simple interest :

principal = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest:"))
time = float(input("Enter the time (in years): "))
simple_interest = principal *rate *time
print(f"The simple Interest is {simple_interest}")

# Question # 4
#speed of an object

distance = float(input("Enter the distance traveled (in meters): "))
time = float(input("Enter the time taken(in seconds): "))
speed = distance / time
print(f"The speed of the object is {speed}m/s")

# Question # 5
#BMI Calculator

weight = float(input("Enter weight in kg : "))
height = float(input("Enter height in meters : "))
bmi = weight/(height*height)
print(f"BMI={bmi}")

# Question # 6
# force using newton's second law

mass = float(input("Enter mass in kg : "))
acc = float(input("Enter accelertaion in m/s^2 : "))
force = mass * acc  
print(f"Force ={force}")  

# Question # 7
# Compound Interest:

p = float(input("principal : "))
r = float(input("rate(decimal) : "))
n = float(input("compounds per year : "))
t = float(input("time in years : "))
A = p*(1+r/n)**(n*t) 
print(f"Total amount ={A}")

# Question # 8
#Perimeter of a Triangle:

a = float(input("side a : ")) 
b = float(input("side b : "))
c = float(input("side c : "))
perimeter = a+b+c
print(f"Perimeter={p}")

# Question # 9
#9) Volume of a Sphere:

r = float(input("Radius: "))
pi=3.1459
volume =(4/3)*pi*(r*r*r)
print(f"Volume={volume}")

# Question # 10
#Kinetic Energy:


mass = float(input("mass (kg): "))
velocity = float(input("velocity (m/s): "))
KE = 0.5 * mass * (velocity * velocity)
print(f"kinetic energy={KE}")

# Question # 11
#Quadratic Equation Roots:

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    # real square root
    root_d = discriminant ** 0.5

    x1 = (-b + root_d) / (2*a)
    x2 = (-b - root_d) / (2*a)

    print(f"Root 1 = {x1}")
    print(f"Root 2 = {x2}")

else:
    # imaginary roots
    real_part = -b / (2*a)
    imaginary_part = ((-discriminant) ** 0.5) / (2*a)

    print(f"Root 1 = {real_part} + {imaginary_part}i")
    print(f"Root 2 = {real_part} - {imaginary_part}i")

# Question # 12
#Temperature Conversion:

C = float(input("Enter temperature in celsius: "))
F = (9/5)*C + 32
print(f"Fahrenheit{F}")

# Question # 13
#Gravitational Force:

G =6.674e-11
m1 = float(input("Mass 1: "))
m2 = float(input("Mass 2: "))
r = float(input("Distance: "))
F = G*m1*m2/(r**2)
print(f"Force ={F}")

# Question # 14
#Volume of a Cylinder:

r=float(input("enter radius:"))
h=float(input("enter height:"))
pi=3.142
square_r=r**2
volume=pi*square_r*h
print(f"volume={volume}")

# Question # 15
#Pressure:

F = float(input("Force: "))
A = float(input("Area: "))

P = F / A
print(f"Pressure = {P}")

# Question # 16
#Electric Power:

V = float(input("voltage: "))
I = float(input("Current: "))
P=V/I
print(f"power ={P}")

# Question # 17
#Perimeter of a Circle (Circumference):

r = float(input("Radius: "))
pi=3.142  
p = 2*pi*r  
print(f"Perimeter = {p}")  

# Question # 18
# Future Value in Savings:

pv=float(input("enter present value:"))
r=float(input("enter anuual rate:" ))
t=float(input("enter years:"))
fv=pv*(1+r)**t
print(f"Future Value ={fv}")

# Question # 19
# Work Done by a Force:

f = float(input("Enter force: "))
d = float(input("Enter distance: "))
theta = float(input("Enter angle (in degrees): "))
rad = theta * 3.14159 / 180
cos_theta = 1 - (rad*rad)/2 + (rad**4)/24   
W = f * d * cos_theta
print(f"Work done ={W}")

# Question # 20
#Heat Transfer:

m = float(input("Mass: "))
c = float(input("Specific Heat: "))
T = float(input("Temperature Change: "))

Q = m * c * T
print(f"Heat ={Q}")

