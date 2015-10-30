def isPalin(word):
	for i in range(len(word)/2):
		if word[i] != word[-1-i]:
			return False
	return True


def findIndex(word):
	for i in range(len(word)/2):
		if word[i] != word[-1-i]:
			if i == 0:
				removed = word[i+1:]
			else:
				removed = word[:i-1] + word[i+1:]

			if isPalin(removed):
				return i
			else:
				return len(word)-1-i
	return -1


if __name__=="__main__":
	T =	int(raw_input())
	for _ in range(T):
		word = raw_input()
		print findIndex(word)