# For loops are used to execute a block of code multiple times
# Example in printing items in a list

years= [2003,2007,2009]

for i in years:
    print( i)

# Uisng loops to change the elements in lists
 
squares = ['red','yellow','green','purple','orange']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

#Accesing indices through a list
for i, square in enumerate(squares):
    print(i, square)