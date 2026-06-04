class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # s =list(str(num1))+list(str(num2))
        # s = [int(c) for c in s]
        count=0
        # print(s)
        # for i in range(1,len(s)-1):
        #     if (s[i]>s[i+1] and s[i]>s[i-1]) or (s[i]<s[i+1] and s[i]<s[i-1]):
        #         count+=1
        # return count


        for num in range(num1,num2+1):
            if num<100:
                continue
            dig1=num%10
            num//=10
            while num>9:
                dig2=num%10
                num//=10
                dig3=num%10
                # num//=10
                print(dig1, dig2, dig3)
                if (dig1>dig2 and dig3>dig2) or (dig1<dig2 and dig3<dig2):
                    count+=1
                dig1=dig2
                
        return count
