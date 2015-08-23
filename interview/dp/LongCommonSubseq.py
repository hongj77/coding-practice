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

if __name__=="__main__":
  a = "ABCDGH"
  b = "AEDFHR"
  print lcs(a,b)
