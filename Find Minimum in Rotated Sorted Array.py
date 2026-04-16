class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            # If sorted range, return first element
            if nums[left] <= nums[right]:
                return nums[left]
            
            mid = left + (right - left) // 2
            
            # Minimum in right half (rotation point after mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            # Minimum in left half (including mid)
            else:
                right = mid
        
        return nums[left]
