if __name__=="__main__":
  N, K = map(int, raw_input().split())
  nums = (map(int, raw_input().split()) for _ in range(N))
  H, C = zip(*nums)

  dp = [0 for _ in range(N)]
  colors = {}
  
  # base case
  colors[C[0]] = True
  if len(colors) == K:
    dp[0] = 1

  print max(dp)
  return

  for i in range(1,N):
    # include or not include
     
    # update the color 
      
     



