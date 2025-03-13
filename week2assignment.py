# empty list 
my_list = []
#append the elements to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# insert a value to second position
my_list.insert(1,15)
# extend the list with another
my_list.extend([50,60,70])
# remove my last element from list
my_list.pop()
# sort the list in ascending order
my_list.sort()
# print the index of value 30
print("The index of value 30 is :",my_list.index(30))

#print the final list
print("The final my_list is:", my_list)