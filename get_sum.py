"""Reflection
It's still not clear to me why we're using a 0 to compare against the current
slice.

I also haven't reviewed the other two O(n^2) and O(n^3) solutions

If all the numbers in the array are positive, then we just need to sum all the 
numbers. The negative numbers cause us to begin checking sequences.

You forgot your edge cases again!!!
"""
def get_sum1(lst):
	""" This doesn't really work if the array contains all negative numbers"""

	max_slice = lst[0]
	current_slice = lst[0]

	for num in lst:
		current_slice = max(current_slice + num, 0)
		max_slice = max(current_slice, max_slice)

	return max_slice

print get_sum1([ -10, -1])


def get_sum2(lst):
	"""This is the Udemy solution"""
	if len(lst) == 0:
		return None

	max_sum = current_sum = lst[0]

	for num in lst[1:]:
		current_sum = max(current_sum + num, num)

		max_sum = max(current_sum, max_sum)

	return max_sum


print get_sum2([1, 2, -10, 3, 4, 10, 10, -10, -1, 20])



