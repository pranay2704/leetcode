class Solution:
    def spl(self,m,n,mat):
        for i in range(len(mat)):
            if i!=m and mat[i][n]==1:
                return False
        for j in range(len(mat[0])):
            if j!=n and mat[m][j]==1:
                return False
        return True        

    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    if self.spl(i,j,mat):
                        count+=1
        return count
      
