import sys

#python implementation of bst

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        node_q = []
        data_list = []
        temp = root
        
        while temp:
            data_list.append(temp.data)
            if temp.left is not None:
                node_q.append(temp.left)
            if temp.right is not None:
                node_q.append(temp.right)
            if len(node_q) == 0:
                break
            temp = node_q.pop(0)
            
        print(' '.join(list(map(str, data_list))))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
