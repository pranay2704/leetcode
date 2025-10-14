"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        # code here
        total=0
        
        def check(self, root1):
            total1=0
            if root1.data>=l:
                if root1.data<=r:
                    total1=root1.data
                    if root1.left!=None:
                        total1+=check(self, root1.left)
                    if root1.right!=None:
                        total1+=check(self, root1.right)
                elif root1.left!=None:
                    total1=check(self, root1.left)
            elif root1.right!=None:
                total1=check(self, root1.right)
            return total1
        if root!=None:
            total=check(self, root)
            return total
        else:
            return 0
                
        
        
