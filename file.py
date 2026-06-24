f = open("basics/file.txt")
data = f.read()
print(data)
f.close()

#File write 
string = "Pankaj Jajim"
f = open("basics/myfile.txt", "w")

f.write(string)
f.close()

