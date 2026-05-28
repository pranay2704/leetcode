class Solution:
    def suf(self, a, b):
        m=len(a)
        n=len(b)
        k=min(m,n)
        count=0
        for i in range(-1,-1-k,-1):
            if a[i]==b[i]:
                count+=1
            else:
                break
        return count
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        res = []
        for i in wordsQuery:
            n=len(i)
            flag=False
            temp = []
            for j in range(len(wordsContainer)):
                if wordsContainer[j] in wordsContainer[j-1:]:

                m=len(wordsContainer[j])
                ln = self.suf(i,wordsContainer[j])
                heapq.heappush(temp, (-ln,m,j))
            res.append(heapq.heappop(temp)[2])
        return res
