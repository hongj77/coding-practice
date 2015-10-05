A = raw_input()
B = raw_input()

Acnt = [0 for _ in range(26)]
Bcnt = [0 for _ in range(26)]

for c in A:
	Acnt[ord(c)-ord('a')] += 1
for c in B:
	Bcnt[ord(c)-ord('a')] += 1

sum = 0
for i in range(26):
	sum += max(Acnt[i], Bcnt[i]) - min(Acnt[i], Bcnt[i])
print sum