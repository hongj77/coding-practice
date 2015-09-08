import sys

if __name__=="__main__":

  n,m = map(int,raw_input().split())
  g = [[0 for i in range(n+1)] for j in range(n+1)]
  out = [0 for i in range(n+1)]

  for _ in range(m):
    node1, node2 = map(int,raw_input().split())
    g[node1][node2] = 1
    g[node2][node1] = 1
    out[node1] += 1
    out[node2] += 1

  min_degrees = sys.maxint

  for i in range(1,n+1):
    for j in range(i+1,n+1):
      if g[i][j] == 1:
        for k in range(j+1,n+1):
          if g[i][k] == 1 and g[j][k] == 1:
            res = out[i] + out[j] + out[k]
            min_degrees = min(min_degrees,res)

  if min_degrees == sys.maxint:
    print -1
  else:
    print min_degrees - 6
