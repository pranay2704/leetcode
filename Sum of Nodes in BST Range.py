"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def nodeSum(self, root, l, r):
        def check(node):
            if not node:
                return 0
            if node.data < l:
                return check(node.right)
            if node.data > r:
                return check(node.left)
            return node.data + check(node.left) + check(node.right)
        return check(root)
                
        
        
