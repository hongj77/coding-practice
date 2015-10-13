# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for _ in xrange(T):
    word = raw_input()
    length = len(word)
    
    count = {}
    for window in range(1,length+1):
        for start in range(length-window+1):
            subword = word[start:start+window]
            wordkey = "".join(sorted(subword))
            if wordkey in count:
                count[wordkey] += 1
            else:
                count[wordkey] = 1
                
    total = 0
    for val in count.values():
        total += ((val-1)*(1+(val-1)))/2

    print total