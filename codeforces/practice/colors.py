
# TLE 
# N <= 5000

if __name__=="__main__":
	N = int(raw_input())
	T = map(int, raw_input().split())

	colors = [0 for _ in range(N)]

	for window in range(1, len(T)+1):
		for i in range(len(T)-window+1):
			sub = T[i:i+window]

			counts = [0 for _ in range(N)]

			for color in sub:
				counts[color-1] += 1

			maxColorCount = -1
			maxColor = -1
			for i in range(len(counts)):
				count = counts[i]
				if count > maxColorCount:
					maxColor = i
					maxColorCount = count

			colors[maxColor] += 1

	color_string = " ".join(map(str, colors))
	print color_string



