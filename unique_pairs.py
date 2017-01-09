"""Reflection

This is the perfect example of a place where it's a really good idea to use a set to 
prevent getting O(n^2) runtime.

Also, remember to add your edge cases!

You thought of the trick to make sure you don't have duplicate pairs in the set. Use 
min / max next time you come across this!"""



def get_pairs(lst, n):
	pairs = set()
	for i in range(len(lst)):
		for j in range(len(lst)):
			if lst[i] + lst[j] == n and i != j:
				if lst[i] > lst[j]:
					pairs.add((lst[j], lst[i]))
				else:
					pairs.add((lst[i], lst[j]))


	return len(pairs)

print get_pairs([1,2,2,3], 4)

#O(N) solution

def get_pairs(lst, n):

	if len(lst) < 2:
		return

	seen = set()
	pairs = set()

	for num in lst:
		if n - num in seen:
			pairs.add(min(num, n - num), max(num, n - num))

		if n - num not in seen:
			seen.add(num)

	return len(pairs)

