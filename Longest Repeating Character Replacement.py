class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        for i in range(len(s)-1):
            j=i+1
            k1=k
            while j<len(s) and (k1>0 or s[j-1]==s[j]):
                if s[i]!=s[j]:
                    k1-=1
                j+=1
            l=max(l,j-i)
        return l
