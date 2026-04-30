class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        def rec(grid, i, j, k):
            if i >= len(grid) or j >= len(grid[0]):
                return -1

            if grid[i][j] > 0:
                if k > 0:
                    k -= 1
                else:
                    return -1

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]

            m1, m2 = -1, -1

            if j < len(grid[0]) - 1:
                right = rec(grid, i, j + 1, k)
                if right != -1:
                    m1 = right + grid[i][j]

            if i < len(grid) - 1:
                down = rec(grid, i + 1, j, k)
                if down != -1:
                    m2 = down + grid[i][j]

            return max(m1, m2)

        return rec(grid, 0, 0, k)
        
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
