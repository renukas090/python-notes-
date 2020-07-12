""" Lambda function: (also known as Anonymous function or function without name)
mostly used in : Django,Machine Learing, Data Science
language use Lambda: java,python/not in c
real use: code optimization

Lambda function: - in python,anonymous function is a function is a function
that is defind without a name.
- anonymous function are created using a keyword "Lambda"
-Lambda takes as any number of arguments and return an evaluated expression.
-Lambda is created without using a def keyword
-We use Lambda function when we require a nameless
 function for a short period of time
 -Lambda Function are used along with builtin function like filter(), map() or
 reduce() etc
 -Advantage of Lambda is taken with with map(),filter() or reduce() function

 # how to create Lambda function & camparison between normal function
 and Lambda function"""


#normal function EXAMPLE:
def square(x):
    return x*x
print("square of a number is ",square(10))
print()
print()
# lambda function
# syntax: arg1,arg2,arg3: expression

square = lambda x1: x1*x1
print("square of a number is ",square(10))
print()
print()

# examples of lambda function:
#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments,
#but can only have one expression.

x = lambda a : a + 10
print(x(5))
print()
print()

#2
x = lambda a, b : a * b
print(x(5, 6))
print()
print()

# 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print()
print()

#4
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
print()
print()

#filter function: the filter() function filters the given sequence with the help
# of a  function that tests each element in the sequence to be true or not
# filter work with condition,without condition it does not work.make code fast

#L={1,2,3...........,20} find list(even or odd number), we use filter here

my_list=[1,5,4,6,8,11,3,12]
new_list=list(filter(lambda x:(x%2==0),my_list))
print(new_list)
print()
print()


##########

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
result = list(filter(lambda x: x % 2, fib))
print(result)
result = filter(lambda x: x % 2 == 0, fib)
result = list(filter(lambda x: x % 2 == 0, fib))
print(result)
print()
print()

#Map function: map() function returns a list of the results after applying
#the given function to each item of a given iterable(list,tuple etc.)
#it work without condition,it check complete list and return
# true or false.

my_list=[1,5,4,6,8,11,3,12]
new_list=list(map(lambda x:(x%2==0),my_list))
print(new_list)
print()
print()


my_list=[1,5,4,6,8,11,3,12]
new_list=list(map(lambda x:(x*2),my_list))
print(new_list)
print()
print()


# normal without using map
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)
print()
print()



########
temp= [39.2, 36.5, 37.3, 37.8]
Fahrenheit = list(map(lambda x: (float(9)/5)*x + 32, temp))
print (Fahrenheit)
C = list(map(lambda x: (float(5)/9)*(x-32), Fahrenheit))
print (C)
print()
print()

#####
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
new_list=list(map(lambda x,y:x+y, a,b))

new_list1=list(map(lambda x,y,z:x+y+z, a,b,c))

new_list2=list(map(lambda x,y,z:x+y-z, a,b,c))
print(new_list2)
print(new_list)
print(new_list1)
print()
print()

#################
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
new_list=list(map(lambda x,y:x+y, a,b))
new_list1=list(map(lambda x,y,z:x+y+z, a,b,c))
new_list2=list(map(lambda x,y,z:x+y-z, a,b,c))
new_list3=list(map(lambda x,y:(y/x==0), a,b))
new_list4=list(map(lambda x,y,z:x*y*z, a,b,c))
new_list5=list(map(lambda x,y,z:x+y*z, a,b,c))
print(new_list)
print(new_list1)
print(new_list2)
print(new_list3)
print(new_list4)
print(new_list5)
print()
print()

 
#Reduce function: reduce function reduce() reduce a value into a single value
#by combinig  elements via a supplied function
#- it is used to reduce multiple list into a single list
#-it does not work directly ,for this you need to import module

# example:
import functools
my_list=[2,4,8,10,12,20]
result=functools.reduce(lambda x,y:(x+y),my_list)
print(result)
print()
print()

####

import functools
my_list=[2,4,8,10,12,20]
result=functools.reduce(lambda x,y:(x*y),my_list)
print(result)
print()
print()

######
import functools
f = lambda a,b: a if (a > b) else b
new_list=functools.reduce(f, [47,11,42,102,13])
print(new_list)
print()
print()

########
import functools
new_list=functools.reduce(lambda x, y: x+y, range(1,101))
print(new_list)
