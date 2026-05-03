class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid={'1','0','8','2','5','6','9'}
        def is_good(self,s):
            lst=set(s)
            print(lst)
            if len(lst.difference(valid))==0 and ('2' in lst or '5' in lst or '9' in lst or '6' in lst):
                return True
            return False
        return sum(1 for i in range(1, n+1) if is_good(self, str(i)))

    
