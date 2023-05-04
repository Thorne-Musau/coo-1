# Different types of data handles in py
# 1. int
print(type(7))
#int holds value of whole numbers
#2. float
print(type(3.0))
#float holds value of decimal numbers
#3.str
print(type('They are coming'))
#str holds the value of characters 
#Others include bool, lists and tuples

# Indexing in strings
name= "Micheal Jackson"
print(name[0])
print(name[-15]) #Negative indexing

#length of string
len(name)

#slicing
name[0:5]

#striding
name[::2]

# concatenation
name= name+ " is the best person i have ever met"
print(name)

#operations include
# upper
print(name.upper())

#lower
print(name.lower())

#replace
new_name= name.replace('Micheal', 'Skai')
print(new_name)

