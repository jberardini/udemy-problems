def bubble_sort(arr):
	for n in range(len(arr) - 1, 0, -1):
		for k in range(n):

			if arr[k] > arr[k+1]:
				arr[k+1], arr[k] = arr[k], arr[k+1]
	return arr


arr = [5, 3, 7, 2]
bubble_sort(arr)

def bubble_sort(arr):

	for n in range(len(arr)-1, 0, -1):
		for k in range(n):
			if arr[k] > arr[k+1]:
				arr[k], arr[k+1] = arr[k+1], arr[k]

	return arr