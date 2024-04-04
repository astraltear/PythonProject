my_list=[ i**2 for i in range(1,11) ]

f = open("output.txt","w")

for item in my_list:
    f.write(str(item))

f.close()


readFile = open("output.txt","r")
print( readFile.read())
print( readFile.readline())


with open("text.txt","w") as textfile:
    textfile.write("Success!!")

print( textfile.closed)
