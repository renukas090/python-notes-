#What are iterators in Python?
#Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.

#Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

#Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

#An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

#The iter() function (which in turn calls the __iter__() method) returns an iterator from them.


##We use the next() function to manually iterate through all the items of an iterator. When we reach
#the end and there is no more data to be returned, it will raise StopIteration. 

my_list = [4, 7, 0, 3]
#my_iter = iter(my_list)
#print(next(my_iter))
#print(next(my_iter))
#print(my_iter.__next__())
#print(my_iter.__next__())
#next(my_iter)




#or we  use
#r=iter(my_list)
#next(r)

###example
my_list = [4, 7, 0, 3,45,67,23,12,45,67]
for i in [my_list]:
    print(my_list)

#>> iter(my_list)
#<list_iterator object at 0x021FA290>
#>>> r=iter(my_list)
#>>> next(r)
#4
 
