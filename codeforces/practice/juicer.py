

if __name__=="__main__":
	N, B, D = map(int, raw_input().split())
	arr = map(int, raw_input().split())

	level = 0
	emptied = 0

	for a in arr:
		if a > B:
			continue
		level += a

		if level > D:
			level = 0
			emptied += 1

	print emptied