import sys



def longestBitonic(a):
  n = len(a)
  # have to build lis[i] where lis[i] is the longest increasing subsequence
  # ENDING with element a[i]
  lis = [1 for _ in range(n)]
  for i in range(n):
    for j in range(i):
      if a[j] < a[i] and lis[j] + 1 > lis[i]:
        lis[i] = lis[j]+1

  # have to build lds[i] where lds[i] is the longest decreasing subsequence
  # STARTING with element a[i]
  lds = [1 for _ in range(n)]
  for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
      if a[i] > a[j] and lds[j]+1 > lds[i]:
        lds[i] = lds[j]+1

  return max(lis[i]+lds[i]-1 for i in range(n))


if __name__=="__main__":
  a = [10,9,8,6,3] 
  b = [1,2,4,101,99,100]
  c = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
  print longestBitonic(c)

