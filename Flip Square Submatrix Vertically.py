class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(x,x+(k//2)):
            grid[i][y:y+k], grid[(2*x)+k-(i+1)][y:y+k] = grid[(2*x)+k-(i+1)][y:y+k], grid[i][y:y+k]
        return grid
