class Solution:
    def kClosest(self, points, k):
        # code here
        res={}
        for i in points:
            if (((i[0]**2)+(i[1]**2))**0.5) not in res:
                res[(((i[0]**2)+(i[1]**2))**0.5)]=[]
                res[(((i[0]**2)+(i[1]**2))**0.5)].append((i[0],i[1]))
            else:
                res[(((i[0]**2)+(i[1]**2))**0.5)].append((i[0],i[1]))
        # print(res)
        final=[]
        res = dict(sorted(res.items()))
        for i in res:
            for j in res[i]:
                if k:
                    final.append(j)
                    k-=1
                else:
                    return final
        return final
        
