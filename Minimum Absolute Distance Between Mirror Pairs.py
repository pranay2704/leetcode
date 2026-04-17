class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        min_dist = n
        df = {}
        for i in range(n):
            if nums[i] in df:
                if min_dist>i-df[nums[i]]:
                    min_dist = i-df[nums[i]]
            s = str(nums[i])
            s = s[::-1]
            s = int(s)
            df[s] = i
        if min_dist==n:
            return -1
        return min_dist
            
