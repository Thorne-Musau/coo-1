#SETS
# 
# Type casting a list
list1= ['rap','house','music','rap']
print(set(list1))

# sets are identiffied by the curly brackets
# Are un orderes and the only contain unique items  
S= { 'A','B','C'}
U ={'A','Z','C'}

# add an element
S.add('added')
# remove an element 
U.remove('Z') 
# finds if element is in list and returns a bool acc
print("added" in S) 


print(U.union(S)) # both lists combined
print(S & U) # intersection of the two lists
U.difference(S)# finds the difference between the two lists
