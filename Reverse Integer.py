class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            s = str(x)
            s = s[:-len(s):-1]
            s = -1 * int(s)
        else:
            s = int(str(x)[::-1])
        if s<(-1*pow(2,31)) or s>(pow(2,31)-1):
            return 0
        return s
