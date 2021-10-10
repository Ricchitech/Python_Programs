#program to count the numbers of characters in the input string.
#length of string

string = input("Enter a string: ")

#method 1 using len() built-in function
print("The length of the string is: ", len(string))
print("\n")

#methd 2 using user defined function
count = 0
for i in string:
    count += 1
print("The length of the string is: ", count)