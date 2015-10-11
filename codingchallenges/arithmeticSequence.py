''' Find the total number of continuous subsequences of an array that is
    an arithmetic sequence
'''

def Sequence(A):

  n = len(A)
  if n < 3:
    return 0
  
  total = 0
  combo = 1
  diff = a[1] - a[0]

  for i in range(n-1):
    if a[i+1] - a[i] == diff and i != n-2:
      combo += 1
    else:
      # combo ended
      if i == n-2:
        combo += 1
      if (combo >= 2 and combo <= 3):
        total += 1
        combo = 1
      elif (combo > 3):
        index = combo + 1
        total_combos = ((index-2) * (1 + index-2)) / 2
        total += total_combos
        combo = 1
      diff = a[i+1] = a[i]
  return total

if __name__=="__main__":
  a = [7,7,7,7,7]
  print Sequence(a)

