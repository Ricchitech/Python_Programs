#String slicing methods for

#string=input("Enter a string:\t")
string="Reva University"
print("The string is:",string)
print("\nAfter applying the slicing on string:")
print("The first character of the string is:",string[0])
print("The last character of the string is:",string[-1])
print("The first three characters of the string are:",string[:3]) #or string[0:3]
print("The last three characters of the string are:",string[-3:])
print("The middle three characters of the string are:",string[3:6])
print("The after three characters of the string are:",string[3:])
print("The Except last  three characters of the string are:",string[:-3])
print("The last three characters of the string are:",string[-3:])
print(string[1:5:2]) #print characters from 1 to 5 and skiping 2 characters
print(string[::-1]) #print the string in reverse order
print(string[::-2]) #print the string in reverse order and skiping 2 characters
print(string[-1:-12:-2]) #print the string in reverse order and skiping 2 characters till 12 characters from last 3 characters
print(string[1::2]) #print the character sequence and skiping 2 characters
print(string[-1:-6:-1]) #print last 6 characters from last character
print("Upper case the first character of the string")
print(string[0].upper())
cap=string.capitalize()
print(cap)
print("Upper case the last character of the string")
print(string[-1].upper())
print("returns True if the string ends with the specified value, otherwise False")
end=string.endswith("!")
print(end)
print("returns True if all the characters are alphabet letters (a-z)")
alpha=string.isalpha()
print(alpha)
print("returns True if all the characters are alphanumeric (a-z, A-Z, 0-9)")
alphanum=string.isalnum()
print(alphanum)
print("returns True if all the characters are digits (0-9)")
digit=string.isdigit()
print(digit)
print("returns a string where all the characters are lowercase")
lower=string.lower()
print(lower)
print("returns a string where all the characters are uppercase")
upper=string.upper()
print(upper)
print("returns a string where all the characters are titlecase")
title=string.title()
print(title)