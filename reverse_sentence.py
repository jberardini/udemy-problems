"""Reflection

Forgot about the option to set through the list backward
"""



import re
def reverse_sentence(sentence):

	sentence = re.sub(' +', ' ', sentence)

	sentence = sentence.split(" ")

	for i in range(len(sentence)/2):
		sentence[i], sentence[-(i + 1)] = sentence[-(i + 1)], sentence[i]

	return sentence

print reverse_sentence('Hi John,     are you ready to')
