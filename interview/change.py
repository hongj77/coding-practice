

# recursive solution
def total(s,m,n):
  if n < 0: return 0
  if n == 0: return 1
  if n > 0 and m < 0: return 0
  return total(s, m-1, n) + total(s, m, n-s[m])


if __name__ == "__main__":
  s = [1,2,3]
  m = len(s)-1
  print total(s, m, 4)
