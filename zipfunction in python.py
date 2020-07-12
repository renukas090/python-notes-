""" Zip function in python: Zip function is used to create a record.
store data in the form of tuple.it works sequentially/every list contain equal element"""
# 1)

id=[11,22,33,44]
name=['amit','raj','bipin','pankaj']
salary=[6000, 6000, 30000, 12500]
city=['noida', 'delhi','gurgaon','jaipur']
for x in zip(id,name,salary,city):
    print(x)
print()
print()


# 2)
id=[11,22,33,44]
name=['amit','raj','bipin','pankaj']
salary=[6000, 6000, 30000, 12500]
city=['noida', 'delhi','gurgaon','jaipur']
combine=zip(id,name,salary,city)
print(type(combine))
print(combine)
print()
print()

# 3)
id=[11,22,33,44]
name=['amit','raj','bipin','pankaj']
salary=[6000, 6000, 30000, 12500]
city=['noida', 'delhi','gurgaon','jaipur']
combine=zip(id,name,salary,city)
combine=list(zip(id,name,salary,city))
print(type(combine))
print(combine)
print()
print()


# 4)
id=[11,22,33,44]
name=['amit','raj','bipin','pankaj']
salary=[6000, 6000, 30000, 12500]
city=['noida', 'delhi','gurgaon','jaipur']
combine=tuple(zip(id,name,salary,city))
print(type(combine))
print(combine)
print()
print()


# 4)
personrecord=((11, 'amit', 6000, 'noida'), (22, 'raj', 6000, 'delhi'),
 (33, 'bipin', 30000, 'gurgaon'),
 (44, 'pankaj', 12500, 'jaipur'))
unzip=tuple(zip(*personrecord))
id=unzip[0]
name=unzip[1]
salary=unzip[2]
city=unzip[3]
print(unzip)
print(id)
print(name)
print(salary)
print(city)
print()
print()


