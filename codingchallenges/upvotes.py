 

def sumsubs(k):
	return ((k-1)*(1+(k-1)))/2


if __name__=="__main__":

	N, K = map(int, raw_input().split())
	a = map(int, raw_input().split())

	for i in range(N-K+1):
		sub = a[i:i+K]
		upcount = 0
		downcount = 0

		combo = 0
		prev = sub[0]
		for j in range(1, len(sub)):
			if sub[j] >= prev:
				combo += 1
			else:
				upcount += sumsubs(combo + 1)
				combo = 0
			if j == len(sub)-1:
				upcount += sumsubs(combo + 1)
			prev = sub[j]

		combo = 0
		prev = sub[0]
		for j in range(1, len(sub)):
			if sub[j] <= prev:
				combo += 1
			else:
				downcount += sumsubs(combo + 1)
				combo = 0
			if j == len(sub)-1:
				downcount += sumsubs(combo + 1)
			prev = sub[j]

		print upcount-downcount






