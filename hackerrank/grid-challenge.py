T = int(raw_input())

for _ in range(T):
  N = int(raw_input())
  G = []
  for _ in range(N):
    G.append(list(raw_input())) 

  for i in range(N):
    for j in range(N-1):
      if ord(G[i][j]) > ord(G[i][j+1]):
        G[i][j], G[i][j+1] = G[i][j+1], G[i][j]

  flag = 1
  for j in range(N):
    for i in range(N-1):
      if ord(G[i][j]) > ord(G[i+1][j]):
        flag = 0
        break

  if flag == 1:
    print "YES"
  else:
    print "NO"

