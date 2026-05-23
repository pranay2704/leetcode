class Solution:
    def check(self, nums: List[int]) -> bool:
        flag=False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if flag==True:
                    return False
                flag=True
                if nums[0]<nums[-1]:
                    return False
        return True
