


if __name__=="__main__":
	n, a = map(int, raw_input().split())
	t = map(int, raw_input().split())

	criminals = 0
	start = a - 1

	if t[start]:
		criminals += 1

	for dist in range(1,n):
		left = start - dist
		right = start + dist

		left_c = False
		left_load = 0
		right_c = False
		right_load = 0

		if left < 0:
			left_c = True
			left_load = 0
		else:
			left_c = t[left]
			left_load = 1

		if right > n-1:
			right_c = True
			right_load = 0
		else:
			right_c = t[right]
			right_load = 1

		if left_c and right_c:
			criminals += left_load + right_load

	print criminals



