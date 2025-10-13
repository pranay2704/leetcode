'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        #code here
        res=[]
        res.append(root.data)
        def nodesum(self, root1):
            if root1.left!=None:
                for i in range(len(res)-1):
                    res.append(res[i]+root1.left.data)
                res.append(root1.left.data)
                nodesum(self, root1.left)
                
            if root1.right!=None:
                for i in range(len(res)-1):
                    res.append(res[i]+root1.right.data)
                res.append(root1.right.data)
                nodesum(self, root1.right)
                
        nodesum(self, root)
        return max(res)
            
