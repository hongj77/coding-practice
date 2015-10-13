# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for _ in range(T):
    word = raw_input()
    length = len(word)
    front = 1
    back = length-2
    
    funny = True
    
    while front <= back:
        val1 = abs(ord(word[front])-ord(word[front-1]))
        val2 = abs(ord(word[back])-ord(word[back+1]))
        if val1 != val2:
            funny = False
            break
        front += 1
        back -= 1
        
    if funny:
        print "Funny"
    else:
        print "Not Funny"