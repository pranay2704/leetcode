class Solution:
    # def rec(self, s, k):
    #     if len(s)<=1:
    #         return k
    #     str1 = ''+s[1:]
    #     return min(self.rec(str1, k), self.rec(str1, k+1))
    def minOperations(self, s: str) -> int:
        str1 = ['0' if i%2==0 else '1' for i in range(len(s))]
        str2 = ['1' if i%2==0 else '0' for i in range(len(s))]
        c1=0
        c2=0
        for i in range(len(s)):
            if str1[i]!=s[i]:
                c1+=1
            if str2[i]!=s[i]:
                c2+=1
        return min(c1,c2)
