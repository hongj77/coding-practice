''' You are given a library with n words (w[0], w[1], ..., w[n-1]). You choose a word from it and
	each step, remove one letter only if doing so yields another word in the library. What is the
	longest possible chain of these removal steps? '''


def differByOne(word1,word2):
	subsequence = True
	for c in word1:
		if c not in word2:
			subsequence = False
			break
	return subsequence
			

def  longest_chain(w):
	''' First, sort the words by length. Use longest increasing subsequence with the condition
		that it can be part of the final "chain" if there is are w[j] to w[i] such that 
		j < i and w[j] and w[i] differ by one character. Find the length of the longest chain.'''
    words = {}
    for i in range(len(w)):
        if w[i] not in words:
            words[w[i]] = True

    sol = [1 for i in range(len(w))]
    w.sort(key=lambda s: len(s))

    for i in range(len(w)):
    	maxcnt = 0
    	for j in range(i):
    		if len(w[i]) - len(w[j]) == 1:
    			if differByOne(w[j],w[i]):
    				maxcnt = max(maxcnt, sol[j])
    	sol[i] = 1 + maxcnt
    return max(sol)
    

a = ["a", "b", "ba", "bca", "bda", "bdca"] # longest chain is 4
print longest_chain(a)