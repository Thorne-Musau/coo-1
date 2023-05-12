example2= "/home/thorne/Desktop/try.txt"
 
with open(example2, "w") as file2: # write line to file
    file2.write("This is line A\n")
    file2.write("This is line B\n")

with open(example2, "r") as test2:
    print(test2.read())

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open(example2, "w") as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        