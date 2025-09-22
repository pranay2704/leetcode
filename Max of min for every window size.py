 Solution:
    def maxOfMins(self, arr):
       # code here
        res=[]
        for i in range(1,len(arr)+1):
            temp=[]
            for j in range(len(arr)-i+1):
                temp.append(min(arr[j:j+i]))
            # print(temp)
            res.append(max(temp))
        # print(res)
        return res       



