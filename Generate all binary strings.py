class Solution:
    def binstr(self, n):
        # code here
        total=0
        for i in range(n):
            total+=(2**i)
        res=[]
        for i in range(total+1):
            z='0'*(n-len(bin(i)[2:]))
            z+=bin(i)[2:]
            res.append(z)
        return res
