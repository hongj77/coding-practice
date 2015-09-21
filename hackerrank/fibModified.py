

A, B, N = map(int, raw_input().split())

sol = [0 for _ in xrange(N)]

sol[0] = A
sol[1] = B

for i in range(2,N):
	sol[i] = sol[i-1]**2 + sol[i-2]

print sol[N-1]
