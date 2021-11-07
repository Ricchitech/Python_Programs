print("Program to write content into file : ")
poem="Lorem ipsum dolor sit amet, consect et dolore magna"
filein=open("poem.txt","wt")
filein.write(poem)
filein.close()
print("File written successfully")

print("Program to read content From file : ")
fileout=open("poem.txt","rt")
poem=fileout.read()
print(poem)
fileout.close()
print("File read successfully")
print("\n")

print("Program to read content of a file with a read chunk of content : ")
poe=""
fout=open("poem.txt","rt")
chunk=10
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

print("Program to read content using readlines() : ")
fiout=open("poem.txt","rt")
lines=fiout.readlines()
print(lines)
print(len(lines),"Lines read")
fiout.close()
print("File read successfully")
print("\n")