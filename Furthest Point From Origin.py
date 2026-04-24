class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c=0
        c1=0
        for i in moves:
            if i=='R':
                c+=1
            elif i=='L':
                c-=1
            else:
                c1+=1
        return abs(c)+c1
