
def my_sqrt(num):
  if num<0:
    return -1
  half = (num/2) + 1
  for i in range(half):
    if i*i == num:
      return i
    elif i*i > num:
      return i-1
  return i #i exists here

print "normal rounded down", my_sqrt(2)

def sqrt_fast(num):
  start = 0
  end = num
  min_range = .0000001
  #basically saying while end and start are NOT the same
  while end - start > min_range:
    mid = start+((end-start)/2.0)
    #the difference is small enough to the real number..
    pow2 = mid*mid
    if abs(pow2 - num) <= min_range:
      return mid
    elif pow2 < num:
      start = mid
    else:
      end = mid
  return mid
  

#the formula for newton raphson method is x1 = x0 - (f(x)/f'(X))
def sqrt_newtonraphson(n):
  root = 1
  while abs(root*root - n) > 0.000001:
    root = root - ((root*root - n) / (2.*root))
  return root

print sqrt_newtonraphson(6)
print "fast no rounding", sqrt_fast(6)




