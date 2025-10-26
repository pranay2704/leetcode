class Solution:
  def minOperations(self, arr):
    # code here
    total=0
    arr.sort(reverse=True)
    for i in arr:
        total+=i
    
    temp_total=total
    i=0
    while (total/2)<temp_total:
        # print(arr)
        arr[0]/=2
        # print(arr)
        # print("arr - ",arr[i])
        temp_total-=arr[0]
        # print("total - ",total/2," total_temp - ",temp_total)
        i+=1
        arr.sort(reverse=True)
    return i
