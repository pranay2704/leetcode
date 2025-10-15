class Solution:
    def kthSmallest(self, root, k): 
        # code here
        l=0
        def check(root1):
            nonlocal l+=1
            if l==k:
                return root1.data
            if root1.left:
                check(root1.left)
            if root1.right:
                check(root1.right)
        check(root)
        return -1
