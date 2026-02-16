class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str1 = ['' for _ in range(numRows)]
        i=0
        sign = 0
        j = 0
        while(i<len(s)):
            # print(j,'-',i)
            str1[j]+=s[i]
            i+=1
            if sign == 0:
                if j+1>=numRows:
                    sign=1
                    j-=1
                else:
                    j+=1
            else:
                if j-1<0:
                    sign=0
                    j+=1
                else:
                    j-=1

        result = ''
        for str in str1:
            result += (str)
        return result
