#Print the first 10 natural numbers using a for loop
#for i in range(1, 11):
   # print(i)

 #Calculate the sum of all numbers from 1 to a given number using a for loop.
# sum= 0
# n = int(input("Enter a maximum number: "))
# for i in range(0, n):
    # sum=sum+i
# print("Sum of the number 0 to your given number is"+sum)
# n= int(input("enter your number  "))
# r=n%2
# if r==0:
#     print("even")
# else:
#     print("odd")

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to 
# divide by (check). If check divides evenly into
#  num, tell that to the user. If not, print a different appropriate message.

# n= int(input("enter your number: "))
# n2= int(input("Enter your second number: "))
# r1= n%n2
# if r1==0:
#     print("hunxa")
# else:
#     print("hudaina")

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# n= int(input("Enter the number: "))
# b= []
# for i in a:
#     if i<n:
#         b.append(i)
#     else:
#         continue
# print(b)   

# n=int(input("enter the number: "))
# b=[]
# for i in range(1, 101):
#     r=n%i
#     if r==0:
#       b.append(i)
#     else:
#        continue
# print(b)

# w= input("Enter a string: ") 
# b=[]
# for i in w:
#     b.append(i)
# a=b[::-1]
# if b==a:
#   print("pallindrome")
# else:
#   print("hoina")
#Write a Python program to create a class representing a Circle.
#Include methods to calculate its area and perimeter.
# class circle:
#     def __inti__(self,radius):
#         self.r=radius
#     def perimeter(self):
#         self.perimeter=2*3.14*self.r
#         return self.perimeter
#     def area(self):
#         self.area=3.14*self.r*self.r
#         return self.area
# radius=int(input("Enter the radius of the circle: "))
# c=circle()
# c.__inti__(radius)
# a=c.area()
# p=c.perimeter()
# print(f'Area of the circle is {a} and Perimeter of the circle is {p}')


# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age

class car:
    def __init__(self,model,speed,colour):
        self.m=model
        self.s=speed
        self.c=colour
    def show(self):
        print(f"Model:{self.m} Speed:{self.s} colour={self.c}")
model=input("Enter the model: ")
speed=input("enter the speed: ")
colour=input("enter the colour: ")
car1=car(model,speed,colour)
car1.show()

