import matplotlib.pyplot as plt # Importing library

# Object is an instance of a partucular type
# Methods are functions taht every instance of that class or type provides

#creating classes
class Circle(object):

    # Constructor
    def __init__(self,radius ,color):
        self.radius = radius;
        self.colour = color;

    # Method
def add_radius(self,r):
    self.radius=self.radius +r
    return(self.radius)

    #Method
def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


c1= Circle(10,'red') # Creating an object

c1.drawCircle()
print("Radius of the object:" ,c1.radius)

BlueCircle = Circle(radius=100)
BlueCircle.drawCircle()