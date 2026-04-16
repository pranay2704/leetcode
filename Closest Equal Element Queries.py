class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        def mindist(self, i):
            count = 1
            left = (i-1+n)%n
            right = (i+1)%n
            while left!=i and right!=i and left!=right:
                # print(left, right)
                if nums[left]==nums[i] or nums[right]==nums[i]: 
                    return count
                count+=1
                left = (i-count+n)%n
                right = (i+count)%n
            if left!=i and right!=i and nums[left]==nums[i]: 
                return count
            return -1
        res = []
        for j in queries:
            # print('count', j)
            k=mindist(self, j)
            res.append(k)
        return res
