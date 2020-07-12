"""list comprehension provide a concise way to create lists.
it consists of brakets containing an expression followed by a for clause, then zero
or more for or if clauses.
the expression can be  anything,meaning you can put in all kinds of objects in list
. the result will be a new list resulting from evaluting the expression in context
of the for and if clauses which follow it 
#list comprehension are 35% faster than for loop and 45% faster than map function
# syntax: result=[value iteration filter]
#in which first 2 parameter must ,3 parameter is optional(if condition then use)"""
###1)
#without using list comprehension:
mylist=[]
for x in range (1,11):
    mylist.append(x**2)
    print(mylist)
    print()
print()
print()
    
#with using list comprehension:
mylist=[x**2 for x in range(1,11)]
print(mylist)
print()


###2)
#without using list comprehension:
mylist=[]
if x in range(1,20):
    if x%2==0:
        mylist.append(x)
        print(mylist)
        print()
        
    
#with using list comprehension:
mylist=[x for x in range(1,20)if x%2 == 0]
print(mylist)
print()


###3)
#without using list comprehension:

i=[x for x in 'MATHEMATICS' if x in ['A','E','I','O','U'] ]
print(i)
print()



##python code with for loop & LC Implementation
def eg2_for(sentence):
    vowels='aeiou'
    filter_list(vowels)
    for l in sentence:
        if l not in vowels:
            filter_list.append(l)
            return"".join(filter_list)
        
def eg2_lc(sentence):
    vowels='aeiou'
    return "".join([ l for l in sentence if l not in vowels])


sentence='my name is renuka sharma'
print("for_loop result:"+eg2_for(sentence))
print("LC result:"+eg2_lc(sentence))
