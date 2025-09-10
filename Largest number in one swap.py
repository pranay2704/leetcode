class Solution:
    def largestSwap(self, s):
        max=0
        #code here
        for i in range(1,len(s)):
            if s[i]>s[max]:
                max=i
                
        for i in range(1,len(s)):
            if s[i]>s[max]:
                max=i
        a=str(s[0])
        b=str(s[max])
        # print(a,'-',b)
        string=list(s)
        string[0]=b
        string[max]=a
        s=''.join(string)
        return s
