class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        prod = 1
        # grid = [[8,18],[24,20],[9,5],[26,26],[19,19],[20,1],[20,23],[15,19],[24,14],[12,15],[22,3],[22,11],[9,25]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                prod*=grid[i][j]
        # print(prod)
        dic={}
        p = [[ 0 for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] in dic:
                    p[i][j] = dic[grid[i][j]]
                else:
                    p[i][j] = int((prod//grid[i][j])%12345)
        return p
