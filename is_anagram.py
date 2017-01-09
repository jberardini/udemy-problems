"""Reflection:

Two words are anagrams if they contain the same letters with the same frequency

The space and lower case stripping are important

Also, note the edge case. We can win fast if the strings (after removal of spaces) 
aren't the same length.
"""

def is_anagram(s1, s2):

	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()

	if len(s1) != len(s2):
		return False

	count = {}

	for letter in s1:
		count[letter] = count.get(letter, 0) + 1

	for letter in s2:
		if letter not in count:
			count[letter] = 1
		else:
			count[letter] -= 1


	for letter in count:
		if count[letter] != 0:
			return False

	return True

print is_anagram('go d', 'dog')

