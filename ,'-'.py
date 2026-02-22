class Solution:
    def binaryGap(self, n: int) -> int:
        longest,count = 0, 0
        flag = False
        while n>0:
            # print(n,'-',n%2,'-',flag,'-',longest,'-',count)
            if n%2==1:
                if flag and longest<count:
                    longest=count
                flag=True
                count=0
            n=n//2
            
            count+=1
        return longest
        

