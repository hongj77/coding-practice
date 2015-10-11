'''Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1          0     2^0 = 1
   / \
  2   2'      ... .
 / \ / \
3  4 4   3      k     2^k


But the following is not:
    1
   / \
  2   2
   \   \
   3    3

'''


def symmetric(root):
    if root == None:
        return True

    if root.left == None and root.right == None:
        return True          

    mirror = symmetricHelper(root.left, root.right)
    return mirror
 

def symmetricHelper(left, right):
    if left == None and right == None:
        return True
    if left != right:
        return False
    if not symmetricHelper(left.left, right.right):
        return False
    if not symmetricHelper(left.right, right.left):
        return False
    return True
    


'''Given an array of integers, write a function to check if there is a consecutive subarray that sums to 0. 

e.g. 

[1, 5, (4, -2, -2),7, 5] would return true 
               
1   6  10    8   6  13 18 
'''

def sumToZero(arr):
    
    if arr == None:
        return False
        
    seen = set()
    current_sum = 0
    
    for num in arr:
        if num == 0: 
            return True
        
        current_sum += num
        if current_sum not in seen:
            seen.add(current_sum)
        else:
            return True

    return False

