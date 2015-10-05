
T = int(raw_input())
for _ in xrange(T):
	N = int(raw_input())
	A = [0]+map(int, raw_input().split())
	S = [0]

	running_sum = 0
	for i in range(1,N+1):
		running_sum += A[i]
		S.append(running_sum)

	flag = False
	for i in range(1,N+1):
		left = S[i-1]
		right = S[-1] - S[i]
		if left == right:
			flag = True
			break

	if flag:
		print "YES"
	else:
		print "NO"


