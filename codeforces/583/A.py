N = int(raw_input())
N2 = N**2

seenh = [0 for _ in range(N+1)]
seenv = [0 for _ in range(N+1)]
sol = []

for i in range(1,N2+1):
	h, v = map(int,raw_input().split())
	if seenh[h] == 0 and seenv[v] == 0:
		sol.append(i)
		seenh[h] = 1
		seenv[v] = 1

print " ".join(map(str,sol))

