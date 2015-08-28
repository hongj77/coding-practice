

if __name__=="__main__":
  size_a, size_b = map(int, raw_input().split()) 
  k, m = map(int, raw_input().split())
  A = list(map(int, raw_input().split()))
  B = list(map(int, raw_input().split()))

  if A[k-1] < B[size_b-m]:
    print "YES"
  else:
    print "NO"


