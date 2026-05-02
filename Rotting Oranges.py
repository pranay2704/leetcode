class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot(self, lst):
            if len(lst)==0:
                return []
            lst_tmp=[]
            for i,j in lst:
                print(i,j)
                if i>0:
                    if grid[i-1][j]==1:
                        grid[i-1][j]=2
                        print("i>0")
                        lst_tmp.append((i-1,j))
                if j>0:
                    if grid[i][j-1]==1:
                        grid[i][j-1]=2
                        print("j>0")
                        lst_tmp.append((i,j-1))
                if i<len(grid)-1:
                    if grid[i+1][j]==1:
                        grid[i+1][j]=2
                        print("i<len(grid)-1")
                        lst_tmp.append((i+1,j))
                if j<len(grid[0])-1:
                    if grid[i][j+1]==1:
                        grid[i][j+1]=2
                        print("j<len(grid[0])-1")
                        lst_tmp.append((i,j+1))
            if len(lst_tmp)==0:
                return []
            new=rot(self,lst_tmp)
            if new==[]:
                return [lst_tmp]
            else:
                lst_tmp=[lst_tmp]
                lst_tmp.extend(new)
            print(lst_tmp,"\n")
            return lst_tmp

        flag=False
        lst = []
        lst_1=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    lst.append((i,j))
                if grid[i][j]==1:
                    flag=True
                    lst_1.append((i,j))
        if flag:
            z=rot(self, lst)
            k=len(z)
            flat = [item for sublist in z for item in sublist]
            print("flat",flat)
            print("lst_1",lst_1)
            if len(flat)!=len(lst_1):
                return -1
            return k
        return 0
        
