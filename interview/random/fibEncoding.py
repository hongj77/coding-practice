# Complete the function below.
from pprint import PrettyPrinter

pp = PrettyPrinter()

def processFib(n):
    fib = {}
    fib[1] = 1
    fib[2] = 2
    for i in range(3,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib


def  encodeFibonacci( n):
    fib = processFib(30) 
    maxn = 0
    for i in range(1,30):
        if fib[i] > n:
            maxn = i
            break

    sol = [[0 for i in range(maxn+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,maxn+1):
            if i - fib[j] < 0:
                sol[i][j] = 0
            elif i - fib[j] == 0:
                sol[i][j] = 1
            else:
                able = False
                for col in range(1,maxn+1):
                    if j == col:
                        continue
                    if sol[i-fib[j]][col] == 1:
                        able = True
                        break
                if able == True:
                    sol[i][j] = 1
                else:
                    sol[i][j] = 0

    res = ""
    row = n
    pp.pprint(sol)
    while row > 0:
        for i in range(len(sol[row])-1, 0, -1):
            if sol[row][i] == 1:
                res += "1"
                row -= fib[i]
            else:
                res += "0"
    return res
    
print encodeFibonacci(3)  

