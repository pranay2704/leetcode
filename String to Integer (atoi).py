class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        sign=1
        if s[0]=='-':
            sign=-1
            s=s[1:]
        elif s[0]=='+':
            sign=1
            s=s[1:]    
        for c in range(len(s)):
            if s[c].isnumeric()==False:
                s=s[:c]
                break
        if len(s)==0:
            return 0
        i = int(s)*sign
        if i > ((2**31)-1):
            return (2**31)-1
        elif i < (-(2**31)):
            return (-(2**31))
        return i
