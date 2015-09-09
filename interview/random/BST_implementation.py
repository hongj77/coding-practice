class BST:
  def __init__(self):
    self.root = None
    self.size = 0
  def length(self):
    return self.size
  def __len__(self):
    return self.size
  def __iter__(self):
    return root.self.__iter__()

class TreeNode:
  def __init__(self, key, val, left=None, right=None, parent=None):
    self.key = key
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent
  def hasLeftChild(self):
    return self.left
  def hasRightChild(self):
    return self.right
  def isLeftChild(self):
    return self.parent && self.parent.left == self
  def isRightChild(self):
    return self.parent && self.parent.right == self
  def isRoot(self):
    return not self.parent
  def isLeaf(self):
    return not (self.left or self.right)
  def hasAnyChildren(self):
    return self.left or self.right
  def hasBothChildren(self):
    return self.left && self.right
  def replaceNodeData(self,key,value,lc,rc):
    self.key = key
    self.val = value
    self.left = lc
    self.right = rc
    if self.hasLeftChild():
        self.leftChild.parent = self
    if self.hasRightChild():
        self.rightChild.parent = self