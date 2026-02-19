class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                str1=s[i:j]
                z=str1[:((j-i)//2)]
                # print(str1)
                if str1.count('0')==str1.count('1') and (z.count('1')==0 or z.count('0')==0):
                    # print("success")
                    res+=1
        return res
