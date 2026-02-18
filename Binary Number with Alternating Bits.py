class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n<=1:
            return True
        z = n%2
        n//=2
        while n>0:
            temp = n%2
            n//=2
            if z==temp:
                return False
            z=temp
        return True
