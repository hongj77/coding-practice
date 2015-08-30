import sys


maxGlobal = -sys.maxint-1

def maxSum(a,n):
  if n == 0:
    return 0
  maxEndingHere = a[n-1]
  for i in range(1,n):
    res = maxSum(a,i)
    if a[i-1] < a[n-1]:
      maxEndingHere = max(maxEndingHere, res+a[n-1])
  
  global maxGlobal
  maxGlobal = max(maxGlobal,maxEndingHere)
  return maxEndingHere


def maxSumDP(a):
  n = len(a)
  sol = [a[i] for i in range(n)]
  for i in range(n):
    for j in range(i):
      if a[j] < a[i] and sol[i] < sol[j]+a[i]:
        sol[i] = sol[j]+a[i]
  return max(sol)


if __name__=="__main__":
  a = [10,5,4,3,2]
  b = [1,101,2,3,100,4,5]
  maxSum(a,len(a))
  print maxGlobal
  maxSum(b,len(b))
  print maxGlobal

  print maxSumDP(b)
  
