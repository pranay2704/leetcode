class Solution:
    def diameter(self, V, edges):
        # Code here
        
        
        p={}
        def longest_edge(i):
            p[i]=0
            flag=0
            max2=0
            for z in edges:
                if z[0]==i:
                    flag=1
                    tmp=longest_edge(z[1])+1
                    k.append(tmp)
                    if max2<tmp:
                        max2=tmp
            k.sort()
            for o in range(len(k)):
                if o<2:
                    p[i]+=k[o]
            if flag:
                return max2
            else:
                return 0
        max1=0    
        for j in range(V):
            if j not in p:
                maxx=longest_edge(j)
            else:
                
                maxx=p[j]
            if maxx>max1:
                max1=maxx
        return max1
            
