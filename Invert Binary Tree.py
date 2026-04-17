# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(self, r1):
            if r1.left!=None:
                rev(self, r1.left)
            if r1.right!=None:
                rev(self, r1.right)
            r1.left, r1.right = r1.right, r1.left
        if root!=None:
            rev(self,root)
        return root
