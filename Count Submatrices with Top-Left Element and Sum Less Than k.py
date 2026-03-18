class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=grid[i][j-1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i>0:
                    grid[i][j]+=grid[i-1][j]
                if grid[i][j]<=k:
                    count+=1
                else:
                    continue
                
        return count
        
