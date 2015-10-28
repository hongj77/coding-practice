
""" Naive implementation of suffix array. O(n^2 * Log(n)) 
	String comparison takes n while sorting takes n log n """


def build_suffix_array(word):
	""" Build an array of all suffixes and sort """

	suffixes = []

	for i in range(len(word)):
		suffix = word[i:]
		suffixes.append((suffix, i))

	suffixes.sort()
	suffix_array = map(lambda tup: tup[1], suffixes)

	return suffix_array
	

def search_suffix(suffix_array, word, pattern):
	""" Search a pattern in O(m*Log(n)), m = length of pattern.
		At most log(n) steps, with m operations per step for string cmp """

	if len(suffix_array) < 1:
		return []

	begin, end = 0, len(suffix_array)-1

	while begin <= end:
		mid = begin+(end-begin)/2 # because of possible overflow
		index = suffix_array[mid]
		suffix = word[index:]

		if pattern == suffix:
			return "Pattern '{}' found at index {} of {}".format(pattern, index, word)
		elif pattern > suffix:
			begin = mid + 1
		elif pattern < suffix:
			end = mid - 1

	return "Pattern '{}' not a suffix of '{}'".format(pattern, word)


if __name__=="__main__":
	word = "hong"
	suffix_array = build_suffix_array(word)
	print "Suffix array is:", suffix_array

	pattern = "ng"
	pattern2 = "nice"

	print search_suffix(suffix_array, word, pattern)
	print search_suffix(suffix_array, word, pattern2)




