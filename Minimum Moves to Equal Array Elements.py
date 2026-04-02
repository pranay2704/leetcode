class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mini = nums[0]
        counter=0
        for i in range(len(nums)):
            if mini<nums[i]:
                mini=nums[i]
        for i in range(len(nums)):
            counter+=abs(mini-nums[i])
        return counter
