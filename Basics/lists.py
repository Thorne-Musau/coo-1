#Lists are also a python data structure
list1=["Micheal",10.1,1982,'Mj', 1] # creating a list data structure in python

# list operations
# slicing
print(list1[3:5])

# As compared to tuples, lists are mutable hence 
# we can perform operations

list1.extend(['pop',10])
print(list1) #extend adds new elements into the list

list2= list1.append(['pop',10]) 
print(list2) # append adds one element into the list

# changing a particular element in an index
list1[0]="Giannah"
print(list1)

#deleting from an element from a list using indexing
del(list1[2])
print(list1)
