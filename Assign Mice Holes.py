class Solution:
    def assignHole(self, mices, holes):
        # code here
        holes.sort()
        mices.sort()
        # print(mices,'\n',holes)
        total=0
        for i in range(len(mices)):
            total = max(abs(holes[i]-mices[i]), total)
        return total
