"""Staircase problem, but is the same as the coin change problem. Given a list of steps you can take, give all possible paths to the top of the staircase of sign n"""

def recursive_staircase(steps, current_level, n):
  """Recursive solution to the staircase problem, top down"""
  if n < 0:
    return 0
  if n == 0:
    return 1
  if len(steps) == 0:
    return 0

  current_step = steps[-1]

  # all the ways with using current step + all the ways without using current step
  return recursive_staircase(steps[:len(steps)-1], current_level+current_step, n-current_step) + \
         recursive_staircase(steps[:len(steps)-1], current_level, n)

if __name__=="__main__":
  steps = [1,2,3,4]
  print recursive_staircase(steps, 0, 5)
