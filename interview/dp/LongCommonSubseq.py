''' Given two sequences, find the length of the longest subsequence present
    in both of them.
'''

''' DP solution runs in O(|a|*|b|). Comparing each of the last characters
    from string a and string b, we know that they can either match or not
    match. If they do NOT match, then either the last char in string a 
    matches some other char earlier in b or the last char in string b
    matches some other char earlier in a. We ensure longest matching
    subsequence by starting comparison from the back of the string. 
'''
def lcs(a,b):  
  # a x b matrix, but with extra row and column for empty chracters
  sol = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
  for i in range(len(a)):
    for j in range(len(b)):
      if a[i] == b[j]:
        sol[i+1][j+1] = sol[i][j] + 1
      else:
        sol[i+1][j+1] = max(sol[i][j+1], sol[i+1][j])
  return sol[len(a)][len(b)] 

''' No wifi today, so will solve a problen by editing this file from
    phone connection. Shortest distance matrix problem you start at 
    0,0 and traverse down right or downright diagnol.
'''

def shortest(cost):
  m = len(cost)
  n = len(cost[0])
  sol[0][0] = cost[0][0]
  for i in range(1,m):
    sol[i][0] = sol[i-1][0] + cost[i][0]
  for i in range(1,n):
    sol[0][i] = sol[0][i-1] + cost[0][i-1]
  for i in range(1,m):
    for j in range(1,n):
      sol[i][j] = min(sol[i-1][j], sol[i][j-1], sol[i-1],[j-1])
  return sol[m][n]

''' No wifi again. Just going to do the knapsack problem. Runs
    in O(nW)
'''
def knapsack(W,n,value,weight):
  sol = [[0 for _ in range(len(n)+1)] for _ in range(len(W)+1)]
  for i in range(1,W):
    for j in range(1,n):
      if weight[j-1] > i:
        sol[i][j] = sol[i][j-1]
      else:
        sol[i][j] = max(sol[i][j-1],sol[i-weight[j-1]][j-1]+value[j])
  return sol[W][n]

if __name__=="__main__":
  a = "ABCDGH"
  b = "AEDFHR"
  print lcs(a,b)
