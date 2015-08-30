
import sys

''' Given a rod of length n and array of prices for each length smaller than n,
    determine the maximum value you can get with a rod by cutting the rod into
    smaller pieces and selling the pieces.
    Example:      Length: 1 2 3 4 5 6
                  Prices: 6 5 3 3 1 1 
    The best price is to sell 6 pieces of the rod at 1 length each, for a max 
    profit of 36. 
'''

''' Simple recursive solution. Branching factor is the problem size. 
'''
def cut(n, prices):
  if n == 0:
    return 0
  if n == 1:
    return prices[n-1]

  maxval = -sys.maxint-1
  for i in range(n):
    maxval = max(maxval, prices[i]+cut(n-i-1, prices))
  return maxval

''' DP bottom up. O(N^2) solution
''' 
def cutDP(n,prices):
  sol = [0 for _ in range(n+1)]
  for i in range(1,n+1):
    sol[i] = max(prices[j]+sol[i-j-1] for j in range(i))
  return sol[n]


if __name__=="__main__":
  prices = [1,5,8,9,10,17,17,20]
  print cut(8,prices)
  print cutDP(8,prices)
