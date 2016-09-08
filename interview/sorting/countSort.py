

def countSort(word):
	""" O(n + k) where k is the size of the buckets. Apparently this is the standard
		way to do counting sort, but seems like there is an easier way.. """
	word = word.lower()

	letters = [0 for _ in range(256)]

	for c in word:
		letters[ord(c)] += 1

	for i in range(1, len(letters)):
		letters[i] += letters[i-1]

	output = ["" for _ in word]

	for c in word:
		output[letters[ord(c)]-1] = c
		letters[ord(c)] -= 1

	return "".join(output)

def countSort2(word):
	""" Just inserting the letters based on letter count is easier to understand than
		left-summing to find the exact index, as we did above. """
	word = word.lower()

	letters = [0 for _ in range(256)]

	for c in word:
		letters[ord(c)] += 1

	output = ["" for _ in word]
	outputIndex = 0

	for i in range(len(letters)):
		while letters[i] > 0:
			output[outputIndex] = chr(i)
			outputIndex += 1
			letters[i] -= 1

	return "".join(output)

if __name__=="__main__":
	word = "hongjeon"
	print countSort(word) # eghjnnoo
	print countSort2(word) # eghjnnoo