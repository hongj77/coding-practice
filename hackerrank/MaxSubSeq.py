# Enter your code here. Read input from STDIN. Print output to STDOUT

def maxContiguous(ls):
    n = len(ls)
    sol = [ls[i] for i in range(n)]
    for i in range(1,n):
        if sol[i-1] + ls[i] > ls[i]:
            sol[i] = sol[i-1] + ls[i]
        else:
            sol[i] = ls[i]
    return max(sol)


def maxSubseq(ls):
    n = len(ls)
    maxsum = 0
    for elem in ls:
        if elem > 0:
            maxsum += elem

    if maxsum == 0:
        maxsum = max(ls)

    return maxsum
    

T = int(raw_input())
for _ in xrange(T):
    N = int(raw_input())
    ls = map(int,raw_input().split())
    print maxContiguous(ls), maxSubseq(ls)


    
    