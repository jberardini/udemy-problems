def selection_sort(arr):

	for fill_slot in range(len(arr)-1, 0, -1):

		position_of_max = 0

		for location in range(1, fill_slot + 1):

			if arr[location] > arr[position_of_max]:
				position_of_max = location


		arr[fill_slot], arr[position_of_max] = arr[position_of_max], arr[fill_slot]

	return arr


arr = [5, 8, 3, 10, 1]
selection_sort(arr)

def selection_sort(arr):

	for fill_slot in range(len(arr)-1, 0, -1):

		position_of_max = 0

		for location in range(1, fill_slot+1):

			if arr[location] > arr[position_of_max]:
				position_of_max = location

		arr[position_of_max], arr[fill_slot] = arr[fill_slot], arr[position_of_max]