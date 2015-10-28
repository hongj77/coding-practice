
def subsetSum(nums,i,k):
	''' Runs in O(2^n) '''
	if k == 0:
		return True
	if i == 0:
		return False
	# include ith element and not include ith element
	return subsetSum(nums,i-1,k-nums[i]) or subsetSum(nums,i-1,k) 


def subsetSumDP(nums,k):
	''' Runs in O(kN) time and space '''
	n = len(nums)
	sol = [[0 for _ in range(n+1)] for _ in range(k+1)]

	# empty set can always sum to 0
	for i in range(n+1):
		sol[0][i] = 1

	# can't sum anything but the empty set without having numbers to sum
	for j in range(1,k+1):
		sol[j][0] = 0

	for i in range(1,k+1):
		for j in range(1,n+1):
			if i - nums[j-1] >= 0:
				# including jth element and not including jth element
				sol[i][j] = sol[i-nums[j-1]][j-1] | sol[i][j-1]
			else:
				# can't include jth element because too large
				sol[i][j] = sol[i][j-1]
	
	return sol[k][n]


a = [1,2,3]
print subsetSum(a,len(a)-1,3)
print subsetSumDP(a,5)