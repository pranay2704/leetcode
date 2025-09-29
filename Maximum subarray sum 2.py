class Solution:
    def maxSubarrSum(self, arr, a, b):
        # code here
        vis=[ 0 for _ in range(len(arr)) ]
        total=sum(arr[:a-1])
        vis[0]=total
        max_total=-100001
        for i in range(a,b+1):
            total=vis[0]+arr[i-1]
            vis[0]=total
            if total>max_total:
                    max_total=total
            for j in range(1,len(arr)-i+1):
                total=vis[j-1]+arr[j+i-1]-arr[j-1]
                vis[j]=total
                if total>max_total:
                    max_total=total
        
        return max_total
