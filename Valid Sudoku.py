class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        grid = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] =='.':
                    continue
                elif (board[i][j] in row[i]) or (board[i][j] in col[j]) or (board[i][j] in grid[3*(i//3)+(j//3)]):
                    return False
                else:
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    grid[3*(i//3)+(j//3)].append(board[i][j])
        print(row,col,grid)
        return True
