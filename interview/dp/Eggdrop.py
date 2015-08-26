import sys

''' The Egg drop question is as follows: Suppose there is a building with
    k floors. The goal is to find the "critical floor" which will break
    the egg when dropped from that floor. If an egg DOES NOT break on floor
    i, then it will not break for all floors below it (0 through i). If an
    egg BREAKS on floor i, then it will break for all floors above it
    (i+1 through k). If an egg does not break on the drop, then it can be 
    reused. However, if an egg breaks, then it is adios amigo for that egg.
    The question, then, is to find this "critical floor" when given a certain
    number of limited eggs with the least drops as possible. 
'''


''' Recursive solution of Egg drop question generalized to n eggs and k floors.
    The goal is to minimize the worst case scenario -- max # of drops until 
    guranteed solution is found. The output is not the critical floor, but
    the maximum number of drops until it is found. This has a branching 
    factor of k, which is very bad.
'''
def eggDrop(n,k):
  # only one possible way to gurantee finding the critical floor with just one 
  # egg. Linear search through 1 to k floors. So the answer is k # of floors.
  if n == 1:
    return k
  # don't need any drops for no floors
  if k == 0:
    return 0
  # To minimize the number of MAX number of drops, we need to find out 
  # what the worst case is for every possibility: egg breaks or it doesn't
  # for every single floor i in 1 ... k
  minTrials = sys.maxint
  for i in range(1,k+1):
    # breaks on i-> n-1 eggs and i-1 floors to check
    # doesn't break on i-> n eggs and k-i floors to check
    worstCase = max(eggDrop(n-1,i-1), eggDrop(n,k-i))
    minTrials = min(minTrials,worstCase)
  return minTrials + 1
  

if __name__=="__main__":
  print eggDrop(2,10)
