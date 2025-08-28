    def maxOnes(self, arr, k):
        # code here
        max_count=0
        for i in range(len(arr)):
            count=k
            j=i
            while count!=0 or arr[j]!=0:
                if arr[j]==0:
                    count-=1
                j+=1
                if j>=len(arr):
                    break
            if (j-i)>max_count:
                max_count=(j-i)
        return max_count
