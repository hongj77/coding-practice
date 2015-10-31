""" Constructing a suffix array in O(N Log^2 N)

	Expliot the fact that all of the sufficies are 
	part of the SAME string, and not some random words.

	If we have the suffixes sorted by their first 2^i 
	characters, we can sort the first 2^i+1 characters of 
	the suffixes in O(N log N) by using mergesort.

	This is because after we have the first 2^i characters sorted,
	the remaining characters in a suffix that's NOT sorted is 
	actually a suffix in the suffix array (since they are all part of the
	same string). That means we can find out the relative order of 
	the remaining characters by looking at what we have already sorted
	for the 2^i first chracters for all the suffixes. The result of sorting 
	again is that now the first 2^i+1 characters are sorted.

	Each sort takes O(N Log N), and there are O(Log N) total sorts
"""

import math
import pprint
pp = pprint.PrettyPrinter()


def build_suffix_array(word):

	N = len(word)
	MAXLG = int(math.ceil(math.log(N,2)))

	# rows are steps, and columns indexed by suffixes
	sortIndex = [[0 for _ in range(N)] for _ in range(MAXLG+1)]

	# in the beginning nothing is sorted
	for i in range(N):
		sortIndex[0][i] = ord(word[i]) - ord('a')


	power_of_two = 1
	steps = 0

	while power_of_two < N:

		# list of 3-tuple 
		# containing rank of ith suffix, 
		# rank of the very next unsorted suffix index,
		# and the number i (denotes the suffix index)
		L = [] 

		for i in range(N):

			if i+power_of_two >= N:
				nextunsorted = -1
			else:
				nextunsorted = sortIndex[steps][i+power_of_two]

			tup = (sortIndex[steps][i], nextunsorted, i)
			L.append(tup)

		L.sort()

		for i in range(N):

			firstIndex, secondIndex, suffixIndex = L[i]

			if i == 0:
				# there was no previous rank
				sortIndex[steps+1][suffixIndex] = 0 
			else:
				firstIndex_prev, secondIndex_prev, suffixIndex_prev = L[i-1]

				# constant amount of compares each time. Just two values
				if firstIndex == firstIndex_prev and secondIndex == secondIndex_prev:
					# share the same rank if the two values are the same as previous suffix
					sortIndex[steps+1][suffixIndex] = sortIndex[steps+1][suffixIndex_prev]
				else:
					sortIndex[steps+1][suffixIndex] = i

		steps += 1
		power_of_two *= 2


	# extract the actual suffix array
	suffix_array = []
	for i in range(N):
		suffix_array.append((i, sortIndex[MAXLG][i]))

	suffix_array.sort(key=lambda tup: tup[1])
	suffix_array = map(lambda tup: tup[0], suffix_array)

	return suffix_array



if __name__=="__main__":
	word = "banana$"
	suffix_array = build_suffix_array(word)
	print "Suffix array is:", suffix_array

	for i in range(int(math.ceil(math.log(len(word),2))),-1,-1):
		print i

