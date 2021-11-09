def print_same_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()


def print_individual_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end="")
        print()


n = int(input("Enter the number of rows: "))
print_same_pattern(n)
print_individual_pattern(n)