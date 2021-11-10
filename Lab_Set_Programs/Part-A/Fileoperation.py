#Program 9 : Program to write the contents into a file and read back the contents

print("Program to write content into file : ")
poem = "REVA University is a private state University located in Bangalore, Karnataka. Reva Group of Educational Institutions was established in 2002, managed by Rukmini Educational Charitable Trust. In 2004 it was taken over by Rukmini Educational Charitable Trust led by Dr. P. Shyama Raju"


# Open file in write mode
filein=open("poem.txt","wt")
filein.write(poem)
filein.close()
print("File written successfully")


# Open file in read mode
print("Program to read content From file : ")
fileout=open("poem.txt","rt")
poem=fileout.read()
print(poem)
fileout.close()
print("File read successfully")
print("\n")


#Using Chunk
print("Program to read content of a file with a read chunk of content : ")
poe=""
fout=open("poem.txt","rt")
chunk=25
while True:
    fragment=fout.read(chunk)
    print(fragment)
    if not fragment:
        break
    poe+=fragment
print(poe)
fout.close()
print("File read successfully")
print("\n")


#readline()
print("Program to read content using readlines() : ")
fiout = open("poem.txt", "rt")
line = fiout.readline()
print(line)
print(len(line), "Lines read")
fiout.close()
print("File read successfully")
print("\n")


#readlines()
print("Program to read content using readlines() : ")
fiout1=open("poem.txt","rt")
lines=fiout1.readlines()
print(lines)
print(len(lines),"Lines read")
fiout1.close()
print("File read successfully")
print("\n")
