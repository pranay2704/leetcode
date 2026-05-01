class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        max_sum=-101*(n**2)
        total_neg = sum(nums)
        total = sum([i*nums[i] for i in range(n)])
        for i in range(n):
            k=total-total_neg+(n*nums[i])
            if k>max_sum:
                max_sum=k
            total=k
        print(n, sum)
        return max_sum
