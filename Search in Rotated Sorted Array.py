class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target==nums[0]:
            return 0
        if target>=nums[0] and target>nums[-1]:
            for i in range(len(nums)-1):
                if nums[i]==target:
                    return i
                if nums[i]>nums[i+1]:
                    return -1
        else:
            for i in range(-1,-len(nums),-1):
                if nums[i]==target:
                    return len(nums)+i
                if nums[i]<nums[i-1]:
                    return -1
        return -1
