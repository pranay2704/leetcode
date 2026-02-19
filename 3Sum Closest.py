class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = 2**31
        total=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    l = nums[i]+nums[j]+nums[k]
                    if abs(target-l)<min_diff:
                        total=l
                        min_diff=abs(target-l)
        return total


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                z=nums[i]+nums[left]+nums[right]
                if z==target:
                    return target
                elif z>target:
                    right-=1
                else:
                    left+=1
                if abs(target-min_diff)>abs(target-z):
                    min_diff=z

        return min_diff
