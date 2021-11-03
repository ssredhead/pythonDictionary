class BinarySearchTree:
    #depth is the tree level it is on. 1 = root level
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None
    
  # Define .insert() below:
  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')  
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)

  def get_node_by_value(self, value):
    if (self.value == value):
      return self
    elif ((self.left is not None) and (value < self.value)):
      return self.left.get_node_by_value(value)
    elif ((self.right is not None) and (value >= self.value)):
      return self.right.get_node_by_value(value)
    else:
      return None
 # Define .depth_first_traversal():
  def depth_first_traversal(self):
    #inorder traversal
    if (self.left is not None):
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if (self.right is not None):
      self.right.depth_first_traversal()
  
root = BinarySearchTree(100)

# Insert values:
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

#output:
# Tree node 50 added to the left of 100 at depth 2
# Tree node 125 added to the right of 100 at depth 2
# Tree node 75 added to the right of 50 at depth 3
# Tree node 25 added to the left of 50 at depth 3
#      100
#     /   \
#   50    125
#  /  \   
# 25  75