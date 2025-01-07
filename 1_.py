# #functions are ways to wrap your code into reusable units 

# #how you define a funciton
# #I only define the function ONCE
# def sayHello():
#     print("say hello")
#     print("Hello Governor")
#     print("Welcome back")    
# #once you define a function you must call oe invoke a function
# #You can do this as many times as you want 
# sayHello()
# sayHello() 
# #whatevers inside the paranthesis is called a parameter
# #a parameter is a place holder for future information
# def sayHello(name):
#     print(f"say hello {name}")
#     print("Hello Governor")
#     print("Welcome back")   
#  #when I pass information in the call function its called an argument
# sayHello("Evins")
# sayHello("Abi")
# #you can have multiple parameters 
# def sayHello(name, age, number):
#     print(f"say hello {name}")
#     print("Hello Governor")
#     print("Welcome back")   
#     print(f"Your age is {age}")
#     print(f"Your number is {number}")

# sayHello("Michelle", 18, 11)

# def determineEligibility(age):
#     #if your age is over 18 you can vote, otherwise you can't
#     if age >= 18:
#         print("You are eligible to vote")
#     else:
#         print("You have to wait")

# determineEligibility(13)
# determineEligibility(19)

# def willYouGraduate(gpa, credits, sat):
#     #gpa:number variable
#     #credits:number variable
#     #passed SAT: boolean
#     if (gpa >= 3.0) and (credits >= 28) and (sat == True):
#          print("You passed! Good luck in college!")
#     elif (gpa < 3.0) or (credits<28) or ( sat != False):
#         print("Back to the drawing board...")
#     else: 
#         print("Talk to your counselor")
    
# willYouGraduate(3.9 , 28, True)
# willYouGraduate(2.1, 3, False)
# willYouGraduate(3.0, 28, True)

    
# return = statement used to end a function and send a result back to the caller

def add (x, y):
    z = x+y 
    return z 

def subtract (x, y):
    z = x-y 
    return z 

def multiply (x, y):
    z = x*y 
    return z 

def divide (x, y):
    z = x/y 
    return z 

#you use print when invoking a function because the return statement only returns information, but it doesn't display anything
print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def createName( first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = createName("spongebob" , "squarepants")
print(full_name)