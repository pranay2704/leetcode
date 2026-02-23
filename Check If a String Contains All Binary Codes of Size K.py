class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # s='00110'
        # k=2
        res = 0
        # for i in range(k):
        #     res+=(2**i)
        count=0
        dic={}
        for i in range(len(s)-k+1):
            if s[i:i+k] not in dic:
                print(s[i:i+k])
                count+=1
                dic[s[i:i+k]] = True
        if count==2**k:
            return True
        return False
