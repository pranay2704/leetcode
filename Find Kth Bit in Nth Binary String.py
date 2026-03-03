class Solution:
    def revinv(self, s):
        s = ''.join('1' if bit == '0' else '0' for bit in s)
        s=s[::-1]
        return s
    def findKthBit(self, n: int, k: int) -> str:
        
        s='0'
        temp=s
        while n>1:
            s = temp+'1'+self.revinv(temp)
            n-=1
            temp=s
        return  s[k-1]
