import math

def same(tup1, tup2):
    sortIndex1, sortIndex2, suffix = tup1
    sortIndex1_prev, sortIndex2_prev, suffix_prev = tup2
    
    if sortIndex1 == sortIndex1_prev and sortIndex2 == sortIndex2_prev:
        return True
    return False


def LCP(x, y, SIndex, maxRows, N):
    count = 0
    for i in range(maxRows, -1, -1):
        if x < N and y < N:
            if SIndex[i][x] == SIndex[i][y]:
                count += 2**(i)
                x += 2**(i)
                y += 2**(i)
    return count


def build(word):
    N = len(word)
    maxRows = int(math.ceil(math.log(N,2)))
    SIndex = [[0 for _ in range(N)] for _ in range(maxRows+1)]
    
    for i, c in enumerate(word):
        SIndex[0][i] = ord(c) - ord('a')
        
    steps = 0
    
    while 2**steps < N:
        L = []
        
        for i in range(N):
            if i + 2**steps < N:
                secondRank = i + 2**steps
                element = (SIndex[steps][i], SIndex[steps][secondRank], i)
                L.append(element)
            else:
                element = (SIndex[steps][i], -1, i)
                L.append(element)
        
        L.sort()
        
        for i in range(N):
            
            if i == 0:
                SIndex[steps+1][L[i][2]] = 0
            else:
                if same(L[i],L[i-1]):
                    SIndex[steps+1][L[i][2]] = SIndex[steps+1][L[i-1][2]]
                else:
                    SIndex[steps+1][L[i][2]] = i
        steps+= 1

    # print SIndex

    totalLCP = len(word)
    for i in range(1,N):
        new = LCP(0,i,SIndex,maxRows, N)
        totalLCP += new
        
    return totalLCP
                
  
    
if __name__=="__main__":
    T = int(raw_input())
    for _ in range(T):
        word = raw_input()
        print build(word)