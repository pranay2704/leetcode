# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        right = []
        lev = [root]
        while lev:
            right.append(lev[-1].val)
            next_lev = []
            for node in lev:
                if node.left!=None:
                    next_lev.append(node.left)
                if node.right!=None:
                    next_lev.append(node.right)
            lev=next_lev
        return right

            
