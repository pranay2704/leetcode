class Solution:
    def nextGreater(self, arr):
        # code here
        # arr1=arr.copy()
        # arr1.sort(reverse=True)
        res=[]
        i=0
        while i<len(arr) and len(res)<len(arr):
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    res+=[arr[j]]
                    break
            if i>=len(res):
                for j in range(i):
                    if arr[j]>arr[i]:
                        res+=[arr[j]]
                        break
            if i>=len(res):
                res.append(-1)
            i+=1
        return res
        
        
        
