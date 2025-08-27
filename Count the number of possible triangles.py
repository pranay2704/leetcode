    def countTriangles(self, arr):
        # code here
        res=0
        arr.sort()
        map={}
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    print(i,'-',j,'-',k)
                    if(arr[i]+arr[j]>arr[k]):
                        res+=1
                    else:
                        break
        return res
