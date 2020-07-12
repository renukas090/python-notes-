#square= lambda x: x*x;
#print(square(2))

my_list=[2,3,4,5,6,7,8,9]
new_list= list(filter(lambda x:(x%2==0),my_list))
new_list1= list(filter(lambda x:(x%2!=0),my_list))
new_list2= list(map(lambda x:(x*2),my_list))


print(new_list)
print(new_list1)
print(new_list2)
