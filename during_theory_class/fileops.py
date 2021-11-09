#Program to write content onto a file.

print("Program to write content onto a file")
content=input("Enter the content to be written: ")
filein=open("file.txt","w") 
#w is for write mode and wt is for text file both are similar
filein.write(content)
filein.close()
print("Content written successfully\n")

#Read 
print("Program to read content From file : ")
fileout = open("file.txt", "r")
data = fileout.read()
print(data)
fileout.close()
print("File read successfully")
print("\n")

#Read With Chunk Data
print("Program to read content of a file with a read chunk of content : ")
dat = ""
fchnk = open("file.txt", "rt")
chunk = 5
while True:
    fragment = fchnk.read(chunk)
    print(fragment)
    if not fragment:
        break
    dat += fragment
print(dat)
fchnk.close()
print("\n")

#readline
print("Program to read content using readline() : ")
freadln = open("file.txt", "r")
lines = freadln.readline()
print(lines)
print(len(lines), "Lines read")
freadln.close()
print("File read successfully")
print("\n")

#readlines
print("Program to read content using readlines() : ")
freadlns = open("file.txt", "r")
lines = freadlns.readlines()
print(lines)
print(len(lines), "Lines read")
freadlns.close()
print("File read successfully")
print("\n")
