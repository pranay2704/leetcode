class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = s[::-1]
        # print(s)
        if len(s)<32:
            s+=('0'*(32-len(s)))
        return int(s, 2)
