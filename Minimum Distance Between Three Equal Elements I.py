class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dist = len(nums)+1
        for i in range(len(nums)-2):
            j=i+1
            while j<len(nums) and dist>=(j-i+1) and nums[i]!=nums[j]:
                j+=1
            if dist<(j-i+1):
                continue
            k=j+1
            while k<len(nums) and dist>=(k-i+1) and nums[i]!=nums[k]:
                k+=1
            if dist<(k-i+1):
                continue
            print(i,j,k,dist)
            if k<len(nums) and j<len(nums):
                dist=min(dist, k-i)
            print("final", i,j,k,dist)
        if dist==len(nums)+1:
            return -1
        return 2*dist
