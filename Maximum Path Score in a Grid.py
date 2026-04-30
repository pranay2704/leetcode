class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        vis=[[-1 for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
        def rec(self, grid, i,j,vis,k):
            if i==len(grid)-1 and j==len(grid[0])-1:
                print("final",i,j,grid[i][j])
                if grid[i][j]>0 and k<=0:
                    return -1
                return grid[i][j]
            if grid[i][j]>0:
                k-=1
            vis[i][j]=1
            m1,m2,m3,m4 = 0,0,0,0

            if j<len(grid[0])-1 and vis[i][j+1]==-1 and k>=0:
                m1 = rec(self,grid,i,j+1,vis,k)+grid[i][j]
                print("M1: ",m1,k)
            if j>0 and vis[i][j-1]==-1 and k>=0:
                m2 = rec(self,grid,i,j-1,vis,k)+grid[i][j]
            if i<len(grid)-1 and vis[i+1][j]==-1 and k>=0:
                m3 = rec(self, grid,i+1,j,vis,k)+grid[i][j]
            if i>0 and vis[i-1][j]==-1 and k>=0:
                m4 = rec(self,grid,i-1,j,vis,k)+grid[i][j]
            print(i,j,m1,m2,m3,m4)
            k1=max(m1,m2,m3,m4)
            print("optimal", i,j,k1)
            return k1
        return rec(self, grid,0,0,vis,k)
