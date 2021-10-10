#program to count number of vowels, consonants and other characters in a string.

string = input("Enter a string: ")
vowels = 0
consonents = 0
others = 0
for i in string:
    if i in "aeiouAEIOU":
        vowels += 1
    elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonents += 1
    else:
        others += 1
print("Number of vowels: ", vowels)
print("Number of consonants: ", consonents)
print("Number of others: ", others)