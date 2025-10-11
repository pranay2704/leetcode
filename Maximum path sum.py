class Solution:
    def findMaxSum(self, root): 
        # code here
        def check(self, root1):
            value=0
            left,right=0,0
            if root1.left!=None:
                z1=check(self, root1.left)
                left=max(0,z1)
            if root1.right!=None:
                z2=check(self, root1.right)
                right=max(0,z2)
            value=root1.data+max(left,right)
            return value
        z=check(self, root)
        return z
