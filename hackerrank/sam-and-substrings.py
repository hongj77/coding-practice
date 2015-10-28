"""
Samantha and Sam are playing a game. They have 'N' balls in front of 
them, each ball numbered from 0 to 9, except the first ball which is 
numbered from 1 to 9. Samantha calculates all the sub-strings of the 
number thus formed, one by one. If the sub-string is S, Sam has to 
throw 'S' candies into an initially empty box. At the end of the game,
am has to find out the total number of candies in the box, T. As T 
can be large, Samantha asks Sam to tell T % (109+7) instead. If Sam 
answers correctly, he can keep all the candies. Sam can't take all 
this Maths and asks for your help. 

Input Format 
A single line containing a string of numbers that appear on the first, 
second, third ball and so on.

Output Format 
A single line which is the number of candies in the box, T % (109+7)

Constraints 
1 ≤ N ≤ 2*105 """


if __name__=="__main__":
	T = raw_input()

	num_list = map(int, list(T))
	dp = [0 for _ in range(len(num_list))]
	dp[0] = num_list[0]

	for i in range(1,len(num_list)):
		temp = (dp[i-1]*10) % (int(1e9)+7)
		dp[i] = ((i+1)*num_list[i] + temp) % (int(1e9)+7)

	print sum(num % (int(1e9)+7) for num in dp)