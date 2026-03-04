class Solution:
    def integ(self,s):
        temp=0
        for c in s:
            for i in range(10):
                if str(i)==c:
                    temp=(temp*10)+i
        return temp
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.integ(num1)*self.integ(num2))
