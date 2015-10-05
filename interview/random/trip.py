
def fib(n):   
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    
    
def fib(n):
    if n==0:
        return 0
    prev = 0
    fib = 1
    for i in range(n):
        temp = fib
        fib = fib + prev
        prev = temp
    return fib
    

def reverse(head):
    newhead = None
    cur_node = head
    while cur_node != None:
        temp = cur_node.next
        cur_node.next = newhead
        newhead = cur_node
        cur_node = temp
        
    return newhead
 
    
def countFive(num, base, k):
    cur_num = abs(num)
    count = 0
    while cur_num != 0:
        if cur_num % base == k:
            count += 1
        cur_num = cur_num / base
    return count

