"""Non-Local keyword:  it works like a global function . but it works for nested
function.
the use of non_local keyword is very much similar to the global keyword. non_local
is used to declare that a variable inside a nested function
(function inside a function) is not local to it,meaning it lies
in the outer inclosing function.if we need to modify the value of non_local
variable in-side a nested function,then we must declare it with non_local
otherwise a local variable with that name is created inside the nested function
"""

def outer_function():
    a=5
def inner_function():
    a=10

    print("outer function:",a)
  
    print("inner function:",a)

inner_function()

outer_function()
print()


#Global::: it works for simple function
# Non-lacal::: it works for nested function

def outer_function():
    a=5
def inner_function():
    nonlocal a
    a=10

    print("outer function:",a)
  
    print("inner function:",a)

inner_function()

outer_function()
