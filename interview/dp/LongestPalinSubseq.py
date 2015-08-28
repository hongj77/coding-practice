import pprint

''' Given a string, find the longest palindrome subsequence.
'''

''' Simple recursive solution. Runs in exponential time due to
    recomputing the same subproblem multiple times.

    We wish to compute the longest palindrome of a string s, which we will
    denote L(0,n-1). The algo is as follows: when given a string 
    s = x_0,x_1,...,x_n-1 compare x_0 == x_n-1. If they are the same,
    then they can ALWAYS add to the size of a smaller palindrome within the
    string. In other words, L(0,n-1) = 2 + L(1,n-2). 

    Otherwise, if x_0 != x_n-1, then we have two cases to check. 
    x_0 might still be part of the longest palindrome, AND
    x_n-1 might also still be part of the longest palindrome. Since we 
    do not know we compute the length of the longest palindromes that involve
    x_0 and the longest palindromes that involve x_n-1 and then take the
    larger one.
'''
def longestPalin(s,start,end):
  # a single letter is a palindrome of length 1
  if start == end:
    return 1
  # two same letter is a palindrome of length 2
  if s[start] == s[end] and end-start == 1:
    return 2
  if s[start] == s[end]:
    return 2 + longestPalin(s,start+1,end-1)

  return max(longestPalin(s,start,end-1),longestPalin(s,start+1,end))

''' DP solution using the same recurisve optimal substructure. 
    Bottom up approaching building a table
'''
def longestPalinDP(s):
  n = len(s)
  sol = [[0 for _ in range(n)] for _ in range(n)]

  # base case of 1
  for i in range(n):
    sol[i][i] = 1

  # filling in the matrix diagonally
  for i in range(1,n):
    for j in range(n-i):
      start = j
      end = start + i
      if s[start] == s[end] and end-start == 1:
        sol[start][end] = 2
      elif  s[start] == s[end]:
        sol[start][end] = 2 + sol[start+1][end-1]
      else:
        sol[start][end] = max(sol[start+1][end],sol[start][end-1])
  return sol[0][n-1]


if __name__=="__main__":
  s = "HONGJEONJEONJEON"
  print longestPalin(s,0,len(s)-1)
  print longestPalinDP(s)
