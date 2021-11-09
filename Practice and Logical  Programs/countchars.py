#count a characters in a string

def countchars(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def main():
    s = input("Enter a string: ")
    d = countchars(s)
    for c in d:
        print("{} occurs {} times".format(c, d[c]))

main()