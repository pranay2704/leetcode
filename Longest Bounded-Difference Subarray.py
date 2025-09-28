class Solution:
    def longestSubarray(self, arr, x):
        #code heret
        vis=[[0 for _ in range(len(arr))] for _ in range(len(arr))]
        start=0
        end=len(arr)-1
        def max_arr(i,j):
            vis[i][j]=1
            z1=arr[i:j+1]
            if (max(z1)-min(z1))<=x:
                return z1
            else:
                z2,z3=[],[]
                if i+1<=j and vis[i+1][j]==0:
                    vis[i+1][j]=1
                    z2=max_arr(i+1,j)
                if i<=j-1 and vis[i][j-1]==0:
                    vis[i][j-1]=1
                    z3=max_arr(i,j-1)
                if len(z3)>=len(z2):
                    return z3
                else:
                    return z2
        return max_arr(start,end)
        
        
        
        
        
        
        
        
        
        
        
        
