#Question # 1
# Area of a rectangle:
# write a python program to calculate the area of rectangle.use the formula
# area=lentgh*widt.

length = float(input("Enter the length of the rectangle: "))  
width = float(input("Enter the width of rectangle: "))
area = length * width  
print(f"The area of a rectangle is {area}")

# Question # 2
#circumference of a circle:
# write a python program to calculate the circumference of a circle.use the formula
# circumference = 2^r
# take the radius r as input from the user 

radius = float(input("Enter the radius of the circle: ")) 
pi = 3.1459
circumference = 2*pi*radius
print(f"The circumference of the circle is{circumference}")

# Question # 3
#simple interest :
#write a python program to calculate the simple interest .use the formula .
#simple interest = principal *rate *time
#take principal ,rate and time as inputs from the user 

principal = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest:"))
time = float(input("Enter the time (in years): "))
simple_interest = principal *rate *time
print(f"The simple Interest is {simple_interest}")

# Question # 4
#speed of an object
#write a python program to calculate the speed of an object, use the formula
# speed = Distance\time
#takedistance and time as inputs from the users

distance = float(input("Enter the distance traveled (in meters): "))
time = float(input("Enter the time taken(in seconds): "))
speed = distance / time
print(f"The speed of the object is {speed}m/s")

# Question # 5
#BMI Calculator
# write a python program to calculate the body mass index (BMI)use the formula BMI=weight(kg)/(height*height) 
#take weight (in kg) and height in meters as in put from the users

weight = float(input("Enter weight in kg : "))
height = float(input("Enter height in meters : "))
bmi = weight/(height*height)
print(f"BMI=,{bmi}")