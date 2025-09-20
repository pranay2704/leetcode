class Solution:
    def longestSubarray(self, arr):
        # code here
        # vis=[[ 0 for _ in range(len(arr))] for _ in range(len(arr)]
        # vis= [[0]*(len(arr))]*(len(arr))
        # max_ij={}
        maxx=0
        def check(self, arr1):
            maxx=0
            max_arr=max(arr1)
            if max_arr<=len(arr1):
                return len(arr1)
            elif len(arr1)>1:
                arr4=[]
                while len(arr1)>0:
                    try:
                        i=arr1.index(max_arr)
                    except:
                        i=-1
                    
                    if i>1:
                        arr4.append(arr1[:i])
                    
                    if i<len(arr1)-1:
                        arr4.append(arr1[i+1:])
                    print(i," 2-",arr1[i+1:])
                    arr1=arr1[:i]+arr1[i+1:]
                    print("1-",arr1)
                for j in arr4:
                    print(" arr4: ",j)
                    zz=check(self,j)
                    if maxx<zz:
                        maxx=zz
                return maxx   
            else:
                return 0
        return check(self,arr)
