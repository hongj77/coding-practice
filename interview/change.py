''' Given a set of coins and amount of money, find the number of possible ways 
    to make change using the coins given'''

# recursive solution
def total(s,m,n):
  if n < 0: return 0
  if n == 0: return 1
  if n > 0 and m < 0: return 0
  return total(s, m-1, n) + total(s, m, n-s[m])

# dp solution
def total2(n,coins):
  m = len(coins)
  sol = [[0 for _ in range(n+1)] for _ in range(m+1)]

  for i in range(n+1):
    sol[0][i] = 0
  for i in range(m+1):
    sol[i][0] = 1
  
  # i is index of coin, j is money
  for i in range(1,m+1):
    for j in range(1,n+1):
      if j - coins[i-1] >= 0:
        # you can use the coin
        # total = ith coin included + ith coin not included
        sol[i][j] = sol[i][j-coins[i-1]] + sol[i-1][j]
      else:
        # you can't use the coin
        # use up to the last coin, then with the same money
        sol[i][j] = sol[i-1][j]
  return sol[m][n]

if __name__ == "__main__":
  s = [1,2,3]

  print total(s,len(s)-1, 5) #recursive test
  print total2(5,s) #dp test
