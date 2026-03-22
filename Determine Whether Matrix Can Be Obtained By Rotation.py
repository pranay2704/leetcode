class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if target==mat:
            return True
        M1 = [[mat[j][i] for j in range(-1, -len(mat)-1,-1)] for i in range(len(mat[0])) ]
        if M1==target:
            return  True
        M2 = [[M1[j][i] for j in range(-1, -len(M1)-1,-1)] for i in range(len(M1[0])) ]
        if M2==target:
            return  True
        M3 = [[M2[j][i] for j in range(-1, -len(M2)-1,-1)] for i in range(len(M2[0])) ]
        if M3==target:
            return  True
        return False
