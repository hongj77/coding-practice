from collections import deque

def countCombos(k):
  return (k**2 - k) / 2

def solve(N,K,A,inc):
  total_counts = [] # indexed by window number
  streaks = deque()

  prev = A[0]
  cur_streak = 1

  # first window is a bit different
  for i in range(1,K):
    num = A[i]

    if inc:
      # non decreasing
      if prev <= num:
        # part of a chain
        cur_streak += 1

      elif prev > num: 
        # now decreasing
        streaks.append(cur_streak)
        cur_streak = 1
    else:
      # non increasing
      if prev >= num:
        # part of a chain
        cur_streak += 1

      elif prev < num: 
        # now decreasing
        streaks.append(cur_streak)
        cur_streak = 1

    prev = num

  # result of first window, and reset  
  streaks.append(cur_streak)

  # add the result of the first window
  current_total = 0
  for elem in streaks:
    current_total += countCombos(elem)

  total_counts.append(current_total)
  r_prev = A[K-1]

  # all other windows, move by one
  cur_streak = 1

  for i in range(1,N-K+1):
    num = A[K+i-1]

    if inc:
      if r_prev <= num: # continue previous streak
        new_r_streak = streaks[-1]+1
        streaks[-1] = new_r_streak
        new_l_streak = streaks[0]-1
        new_count = total_counts[i-1] + (new_r_streak-1) - new_l_streak

      elif r_prev > num: # streak ended, rightmost streak is now 1
        streaks.append(1)
        new_l_streak = streaks[0]-1
        new_count = total_counts[i-1] - new_l_streak

    else:
      if r_prev >= num: # continue previous streak
        new_r_streak = streaks[-1]+1
        streaks[-1] = new_r_streak
        new_l_streak = streaks[0]-1
        new_count = total_counts[i-1] + (new_r_streak-1) - new_l_streak

      elif r_prev < num: # streak ended, rightmost streak is now 1
        streaks.append(1)
        new_l_streak = streaks[0]-1
        new_count = total_counts[i-1] - new_l_streak

    if new_l_streak == 0:
      streaks.popleft()
    else:
      streaks[0] = new_l_streak

    total_counts.append(new_count)
    r_prev = num

  return total_counts


if __name__=="__main__":
  N, K = map(int, raw_input().split())
  A = map(int, raw_input().split())
  inc_total = solve(N,K,A,True)
  dec_total = solve(N,K,A,False)

  for i in range(len(inc_total)):
    print inc_total[i] - dec_total[i]
