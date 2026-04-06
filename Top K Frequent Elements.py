class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        dic = dict(sorted(dic.items(),key = lambda x:x[1],  reverse=True))
        res=[]
        for i,j in dic.items():
            if k>0:
                res.append(i)
                k-=1
        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        dic = list(sorted(dic.keys(),key = lambda x:dic[x],  reverse=True))
        return dic[:k]
