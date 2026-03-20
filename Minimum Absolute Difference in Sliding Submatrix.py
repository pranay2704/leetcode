class Solution:
    def gridmin(self, grid,l,m,k):
        if k<2:
            return 0
        lt = []
        for i in range(l, l+k):
            for j in range(m, m+k):
                if grid[i][j] not in lt:
                    lt.append(grid[i][j])
        if len(lt)<2:
            return 0
        lt.sort()
        print(lt)
        mindiff=200001
        for i in range(len(lt)-1):
            if mindiff>abs(lt[i]-lt[i+1]):
                mindiff=abs(lt[i]-lt[i+1])
        return mindiff

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # grid = [[2,0],[1,8]]
        result = [[0 for i in range(len(grid[0])-k+1)] for i in range(len(grid)-k+1) ]
        for i in range(len(grid)-k+1):
            for j in range(len(grid[0])-k+1):
                result[i][j] = self.gridmin(grid,i,j,k)
        return result
