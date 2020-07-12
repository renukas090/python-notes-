#https://www.python-course.eu/python3_decorators.php
""" Decorater function:{if we want extra functionality in function
then we use decorator function}
decorator is a modify or enhance function. it act as a wrapper for your original
function."""
#decorator use function as a parameter
#so it use(func) as argumentt
#we use @ symbol before any function
#example 1)

def my_decorator(func):
    def wrapper(x,y):
        print("before fuction calling")
        print(func.__name__,'=',func(x,y))
        print("After fuction calling")
        print(func.__name__,'=',func(x,y))
    return wrapper

@my_decorator
def add(a,b):
    print("value of a is: = ",a,","  "value of b is:=",b)
    return a+b

@my_decorator
def sub(a,b):
    print("value of a is: = ",a,","  "value of b is:=",b)
    return a-b

@my_decorator
def mul(a,b):
    print("value of a is: = ",a,","  "value of b is:=",b)
    return a*b

@ my_decorator
def div(a,b):
    print("value of a is: = ",a,","  "value of b is:=",b)
    return a/b


add(10,20)
sub(30,10)
mul(23,2)
div(20,10)

print()
print()

# example (2):

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")
print()
print()


# example (3):

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def succ(n):
    return n + 1

succ(10)
print()
print()


# example (4):
from math import sin, cos

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

sin = our_decorator(sin)
cos = our_decorator(cos)

for f in [sin, cos]:
    f(3.1415)

print()
print()

#example (4):
from random import random, randint, choice

def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

random = our_decorator(random)
randint = our_decorator(randint)
choice = our_decorator(choice)

random()
randint(3, 8)
choice([4, 5, 6])
print()
print()


#example (5):
def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
	print(i, factorial(i))

#print(factorial(-1))
print()
print()


#Counting Function Calls with Decorators: The following example uses a decorator to count
#the number of times a function has been called
#example (6):
def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)
    
print(succ.calls)
print()
print()

#example (7):

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mul1(x, y=1):
    return x*y + 1

print(succ.calls)
for i in range(10):
    succ(i)
mul1(3, 4)
mul1(4)
mul1(y=3, x=2)
    
print(succ.calls)
print(mul1.calls)
