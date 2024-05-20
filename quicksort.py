def quicksort(array, low, high):
	if low < high:

		# Find pivot
		# smaller than pivot on the left
		# greater than pivot on the right
		pi = partition(array, low, high)

		# Recursive left of pivot
		quicksort(array, low, pi - 1)

		# Recursive right of pivot
		quicksort(array, pi + 1, high)


# Driver code
if __name__ == '__main__':
	array = [10, 7, 8, 9, 1, 5]
	N = len(array)

	# Function call
	quicksort(array, 0, N - 1)
	print('Sorted array:')
	for x in array:
		print(x, end=" ")