# Function in python:
# A function is a block of statements which can be used repetitively in a program.
# It savesthe time of a developer.In python concept of function is same as in other 
# langueges.you can pass data ,known as parameters,into a funtion.
# functions help to organize code into logical blocks that perform specific tasks.
# def function_name(parameters): 

# Simple function:

#def simplefunction():
    #print("Hello,World!")
    #simplefunction()

# function with parameters(Arguments):

#def sumdata(a,b):
    #print(a+b)
    
   # n=20
    #n1=50
    #sumdata(n,n1)


   # m1= 10
    #m2=50
    #sumdata(m1,m2)

# function with return value:
def sumdata(a,b):
    c=a+b
    return c
output=sumdata(20,10)
print(output)

def square(x):
    return x*x,x*2
s= square(10)
s1= square(5)
print(s)
print(s1)


    