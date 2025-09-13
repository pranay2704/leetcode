class Solution:
    def minCost(self, n, m, x, y):
        # code here
        ver=1
        hor=1
        i=0
        j=0
        total=0
        x.sort(reverse=True)
        y.sort(reverse=True)
        while i<len(x) or  j<len(y):
            
            if i<len(x) and j<len(y):
                # print(x[i],'i=',i,'  ',y[j],'j=',j,'  total=',total)
                if x[i]>y[j]:
                    total+=(x[i]*hor)
                    ver+=1
                    i+=1
                else:
                    total+=(y[j]*ver)
                    hor+=1
                    j+=1
            elif j<len(y):
                # print(y[j],'j=',j,'  total=',total)
                total+=(y[j]*ver)
                hor+=1
                j+=1
            elif i<len(x):
                # print(x[i],'i=',i,'  total=',total)
                total+=(x[i]*hor)
                ver+=1
                i+=1
        return total
        
        
        
