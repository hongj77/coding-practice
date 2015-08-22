''' Longest increasing subsequence problem. Find the length of the longest increasing
    subsequence such that all elements are sorted in increasing order.
'''


''' recursive solution. The idea is to consider EACH element as the last number of
    the longest subsequence.
'''
def longest(a):
  # ith element is passed in
  def longest_helper(i):
    if i == 0:
      return 1
    maxnum = 0
    for j in range(i):
      # maximum of all numbers that can potentially be a 
      # part of a chain including the ith number
      if a[j] < a[i]:
        maxnum = max(maxnum, longest_helper(j))
    # take the optimal subsolution + 1 in length
    return 1 + maxnum

  return longest_helper(len(a)-1) # start from the last element


''' dp solution. going to use the tabulation method (bottom up) to save and compute 
    answers to subsolutions that are otherwise computed multiple times
    O(N^2) time complexity due to comparing max of all elements before it
'''
def longestdp(a):
  # all elements in the least, can make a subsequence of just themselves
  sol = [1 for _ in range(len(a))] 
  for i in range(len(a)):
    for j in range(i):
      # if you can do better than starting over from 1, then the optimal solution
      # is to take the previous solution and add 1
      if a[j] < a[i] and sol[j]+1 > sol[i]:
        sol[i] = sol[j]+1
  return max(sol)


if __name__=="__main__":
  a = [10,50,11,12,13]
  print longest(a)
  print longestdp(a)
