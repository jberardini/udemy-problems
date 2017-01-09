def compress_str(s):
	new_string = ''
	chars = {}

	for char in s:
		chars[char] = chars.get(char, 0) + 1

	for letter, num in chars.iteritems():
		num = str(num)
		new_string = new_string + letter + num

	print new_string


compress_str('AAAABBBCCCCCCCCDaaa')
