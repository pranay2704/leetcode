class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # grid = [[1,1,1]]
        # if (len(grid)%2!=0) and (len(grid[0])%2!=0):
        #     return False
        row = [0 for _ in range(len(grid))]
        col = [0 for _ in range(len(grid[0]))]
        total_row=0
        total_col=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row[i]+=grid[i][j]
                if j==len(grid[0])-1:
                    total_row+=row[i]                
                col[j]+=grid[i][j]
                if i==len(grid)-1:
                    total_col+=col[j]
        rw=0
        for i in row:
            rw+=i
            if (total_row/2)==rw:
                return True
        cl=0
        for i in col:
            cl+=i
            if (total_col/2)==cl:
                return True
        return False
