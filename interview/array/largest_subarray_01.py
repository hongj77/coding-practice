""" Given an array containing only 0s and 1s, find the largest subarray which contains equal no of 0s and 1s. """

def maxLenArraySumZero(arr):
  """ if we count 0's as -1, then the problem reduces down to finding the 
      max length subarray where where the sum is 0. This solution is O(n) 
      time O(n) memory """
  
  sumArr = [0 for _ in arr]
  sumArr.append(0) # extra element for the 0th special case

  # summing from the left side sumArr[i+1] = arr[0] + ... + arr[i]
  for i in range(len(arr)):
    num = -1 if (arr[i] == 0) else 1
    sumArr[i+1] = num + sumArr[i]
  
  numToMaxIndex = dict() # worst case allocation (max_num - min_num + 1)

  # look for max length of same number
  for i, elem in enumerate(sumArr):
    # store (start, end) of each distinct number
    if elem not in numToMaxIndex:
      numToMaxIndex[elem] = (i,i)
    else:
      start, end = numToMaxIndex[elem]
      if i > end:
        numToMaxIndex[elem] = (start, i)

  # for all intervals find max length
  maxLen = 0
  maxLeft = -1
  maxRight = -1
  print numToMaxIndex
  for key, val in numToMaxIndex.iteritems():
    start, end = val
    currLen = end-start
  
    # takes care of subarrays of length 1
    if currLen > 0 and currLen > maxLen:
      maxLen = currLen
      maxLeft = start
      maxRight = end-1

  print "Max subarray goes from {} to {} with length {}".format(maxLeft, maxRight, maxLen)


if __name__=="__main__":
  test1 = [0,1,1,1,0,0]
  test2 = [0,1,0,0,1,0,0] # length 4
  test3 = [0] # none
  test4 = [1,0,1,1,1,0,0] # 1 to 6
  test5 = [1,1,1,1] # -1 to -1

  maxLenArraySumZero(test1)
  maxLenArraySumZero(test2)
  maxLenArraySumZero(test3)
  maxLenArraySumZero(test4)
  maxLenArraySumZero(test5)

