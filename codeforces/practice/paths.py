# memory limit exceeded
# 64MB

def recurse(i,j, m,n, paths):
	if i > m or j > n:
		return 0

	if i == m and j == n:
		return 1

	possible_i = m-i
	possible_j = n-j

	temp_i = i
	i_res = 0
	for _ in range(possible_i):
		temp_i += 1

		if temp_i not in dp:
			# haven't seen i before
			dp[temp_i] = {}
	
		if j not in dp[temp_i]:
			# haven't seen j before
			dp[temp_i][j] = recurse(temp_i, j, m, n, paths+" ({},{})".format(i,j))

		i_res += dp[temp_i][j]

	temp_j = j
	j_res = 0
	for _ in range(possible_j):
		temp_j += 1	

		if i not in dp:
			dp[i] = {}

		if temp_j not in dp[i]:
			dp[i][temp_j] = recurse(i, temp_j, m, n, paths+" ({},{})".format(i,j))

		j_res += dp[i][temp_j]

	return i_res + j_res



if __name__=="__main__":
	num_rows = 10e6
	m, n = map(int, raw_input().split())

	dp = {} # 2d hash
	print recurse(0,0, m,n, "") % (1000000000 + 7)

