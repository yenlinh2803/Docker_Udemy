f = open("my_file.txt", "r")
lines = f.readline()
for line in lines.split(","):
    print(line)
    print(type(line))

#close file
f.close