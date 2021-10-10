def palindrome(word):
    """
    This function checks if a word is a palindrome.
    """
    if word == word[::-1]:
        return True
    else:
        return False

word=input("Enter a word: ")

palindrome(word)

if True:
    print("The word is a palindrome.")
else:
    print("The word is a palindrome.")