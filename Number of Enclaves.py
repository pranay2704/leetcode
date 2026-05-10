class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m =len(grid), len(grid[0])
        vis=[[0 for _ in range(m)]for _ in range(n) ]
        def bfs(self, i,j):
            if i<0 or j<0 or i>=n or j>=m or vis[i][j]!=0 or grid[i][j]==0:
                return
            # mark 0 the land which are connected to edges 
            grid[i][j]=0
            vis[i][j]=1
            bfs(self, i+1,j)
            bfs(self, i,j+1)
            bfs(self, i,j-1)
            bfs(self, i-1,j)
            return

        total_1 = sum([sum(x) for x in grid])
        #iterate through edges
        for i in range(n):
            bfs(self, i,0)
            bfs(self, i,m-1)                                    
        for j in range(m):
            bfs(self, 0,j)
            bfs(self, n-1,j) 
        
        total_2 = sum([sum(x) for x in grid])
        return total_2
