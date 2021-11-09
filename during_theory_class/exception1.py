try:
    #this will throw an exception if the file is not found
    fileptr=open("file.txt", 'r')
except IOError:
    print("File not found") 
else:
    print("File opened successfully")
    fileptr.close()
