from itertools import combinations
class Solution:
    def sumOfModes(self, arr, k):
        # code here
        arr.sort()
        total=0
        print(arr)
        comb_arr = list(combinations(arr, k))
        for i in comb_arr:
            if k==1:
                return sum(arr)
            elif k==2:
               total=total+i[0]
            elif k%2==0:
                if i[(k/2)-1]==i[(k/2)-2]:
                    total=total+i[(k/2)-1]
                elif i[(k/2)]==i[(k/2)+1]:
                    total=total+i[(k/2)+1]
                else :
                    total=total+i[0]
            elif k%2==1:
                if i[int((k-1)/2)]==i[int((k-1)/2)-1] or i[int((k-1)/2)]==i[int((k-1)/2)+1]:
                    total=total+i[int((k-1)/2)]
                else:
                    total=total+i[0]
                print(i,'-',int((k-1)/2),'-',i[int((k-1)/2)])
            print(total)
        return total
