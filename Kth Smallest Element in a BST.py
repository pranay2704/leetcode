# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root):
        # print(root.val)
        res = []
        if root == None:
            return res
        res1, res2 =[], []
        if root.left!=None:
            res1=self.rec(root.left)
        res.extend(res1)
        res.append(root.val)
        if root.right!=None:
            res2=self.rec(root.right)
        res.extend(res2)
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        res = self.rec(root)
        print(res)
        return res[k-1]
