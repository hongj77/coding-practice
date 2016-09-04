
def int_to_string1(num):
	"""Naive implementation with O(n) string concatenation for a total complexity of O(n^2)"""
	nums = ["0","1","2","3","4","5","6","7","8","9"]
	res = ""

	while num > 0:
		digit = num % 10
		num /= 10
		res = nums[digit] + res

	return res

def int_to_string2(num):
	"""Using char array for join later. total complexity of O(n)"""
	nums = ["0","1","2","3","4","5","6","7","8","9"]
	res = []

	while num > 0:
		digit = num % 10
		num /= 10
		res.append(nums[digit])

	return "".join(res[::-1])

def int_to_string3(num):
	"""Maybe try again without the reverse?"""
	nums = ["0","1","2","3","4","5","6","7","8","9"]

	from collections import deque
	res = deque()

	while num > 0:
		digit = num % 10
		num /= 10
		res.appendleft(nums[digit])

	return "".join(res)

def int_to_string4(num):
	"""Python generator version"""
	def convert(num):
		nums = ["0","1","2","3","4","5","6","7","8","9"]

		while num > 0:
			digit = num % 10
			num /= 10
			yield nums[digit]

	generator = convert(num)
	return "".join(reversed(list(generator))) # lol


print int_to_string1(765)
print int_to_string2(765)
print int_to_string3(765)
print int_to_string4(765)