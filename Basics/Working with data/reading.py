example1= "/home/thorne/Desktop/DSP/Basics/Working with data/example1.txt"

with open(example1 ,"r") as file1:
    Filecontent=file1.read()
    print(Filecontent)
    print(file1.read(17))
    print(file1.readline(17))