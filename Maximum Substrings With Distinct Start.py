class Solution:
    def maxDistinct(self, s: str) -> int:
        char = {}
        count=0
        for i in s:
            if i not in char:
                count+=1
                char[i]=True
        return count
