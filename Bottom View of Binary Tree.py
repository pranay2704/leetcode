'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        res={}
        
        def bottomview(node,start):
            res[start]=node
            if node.left!=None:
                bottomview(node.left,start-1)
            if node.right!=None:
                bottomview(node.right,start+1)
        bottomview(root,0)
        z=list(res.items())
        print(z)
        return [1,2]
        
