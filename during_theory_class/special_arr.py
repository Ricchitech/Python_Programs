#An array has a special integer if that integer can be formed by calculating the sum of a number and its reverse.

#find how many integer are special in the array

#Note: Trailing Zeros from the reverse of a number formed need to be removed if they exist.

#input1: Array of strings where each string represents a number
#input2: Size of the array
#output: Number of special integers in the array


def totalSum(arr, n):

	# Stores the final sum
	sums = 0

	# Traverse the given array
	for i in range(0, n):

		# Stores count of ending 0s
		count = 0
		rev = 0
		num = arr[i]

		# Flag to avoid count of 0s
		# that doesn't ends with 0s
		f = False

		while num > 0:

			# Count of ending 0s
		    while (num > 0 and f == False and num % 10 == 0):
				count += 1
				num //= 10

			    # Update flag with true
			    f = True

			    # Reversing the num
			    if num > 0:
				    rev = rev * 10 + num % 10
				    num //= 10

		# Add all ending 0s to
		# end of rev
		if (count > 0):
			rev = rev * pow(10, count)

			# Update sum
		sums = sums + rev

	# Print total sum
	print(sums)


# Driver Code
if __name__ == "__main__":

	# Given arr[]
	arr = [7, 234, 58100]

	n = len(arr)

	# Function call
	totalSum(arr, n)

# This code is contributed by akhilsaini
