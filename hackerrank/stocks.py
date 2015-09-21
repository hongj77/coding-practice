T = int(raw_input())

for _ in xrange(T):
	N = int(raw_input())
	ls = map(int, raw_input().split())

	maxarray = [0 for _ in xrange(N)]
	maxarray[N-1] = ls[N-1]
	for i in range(N-2,-1,-1):
		maxarray[i] = max(maxarray[i+1],ls[i])

	profit = 0
	for i in range(N):
		profit += maxarray[i] - ls[i]

	print profit
