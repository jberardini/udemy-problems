def find_missing(lst1, lst2):
	"""My first try. O(n^2)"""

	for num in lst1:
		if num not in lst2:
			return num

print find_missing([1,2,3,4,5,6,7], [3,7,2,1,4,6])

def find_missing2(lst1, lst2):
	"""Iterating through the dictionary is uncessary. See below"""

	count = {}

	for num in lst1:
		count[num] = count.get(num, 0) + 1

	for num in lst2:
		count[num] -= 1

	for num in count:
		if count[num] > 0:
			return num

print find_missing2([1,2,3,4,5,6,7], [3,7,2,1,4,6])


def find_missing3(lst1, lst2):
	"""Good linear solution, but slightly more space complexity"""

	count = {}

	for num in lst2:
		count[num] = count.get(num, 0) + 1

	for num in lst1:
		if num not in count:
			return num

		else:
			count[num] -= 1

print find_missing3([1,2,3,4,5,6,7], [3,7,2,1,4,6])

def find_missing4(lst1, lst2):
	"""Clever solution using bitwise operators. O(N)"""

	result = 0

	for num in lst1 + lst2:
		result ^= num
		
	return result

print find_missing4([1,2,3,4,5,6,7], [3,7,2,1,4,6])



def find_missing5(lst1, lst2):
	"""This is O(nlogn) because of the sorting"""
	lst1.sort()
	lst2.sort()

	for num1, num2 in zip(lst1, lst2):
		if num1 != num2:
			return num1

	return arr1[-1]

print find_missing5([1,2,3,4,5,6,7], [3,7,2,1,4,6])
