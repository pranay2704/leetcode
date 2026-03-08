class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k=sum((2**i for i in range(len(nums[0])) ))
        for i in range(k+1):
            str1 = bin(i)[2:]
            str1 = ('0'*(len(nums[0])-len(str1))) + str1
            if str1 not in nums:
                return str1
