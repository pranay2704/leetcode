class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check2(self, str1):
            for i in dictionary:
                if i==str1:
                    return True
                else:
                    count=0
                    for j in range(len(i)):
                        if str1[j]!=i[j]:
                            count+=1
                            if count>2:
                                break
                            
                    if count<3:
                        return True
            return False
        res=[]
        for k in queries :
            if check2(self, k):
                res.append(k)
        return res
                            
