class Solution:
    def maxArea(self, mat):
        # code here
        vis=[[0]*len(mat[0])]*len(mat)
        # print(vis)
        def check_max(arr1,i,j):
            if vis[i][j]:
                return vis[i][j]
            elif arr1[i][j]==1:
                min_row,min_col=1001,1001
                for j1 in range(j,len(arr1)):
                    row=i
                    while arr1[row][j1]==1 :
                        if row<(len(arr1)-1):
                            row+=1
                        else:
                            break
                    if min_row>row:
                        min_row=row
                for i1 in range(min_row,i-1,-1):
                    col=j
                    while arr1[i1][col]==1:
                        if col<(len(arr1[0])-1):
                            col+=1
                        else:   
                            break
                    if min_col>col:
                        min_col=col
                z1=((min_row-i+1)*(min_col-j+1))
                z2,z3=0,0
                if i<(len(arr1)-1):
                    z2=check_max(arr1,i+1,j)
                if j<(len(arr1[0])-1):
                    z3=check_max(arr1,i,j+1)
                # print('i ',i,' j ',j,' ',((min_row-i+1)*(min_row-j+1)),' z1 ',z1,' z2 ',z2,' z3 ',z3)
                vis[i][j]= max(z1,z2,z3)
                return vis[i][j]
            else:
                z2,z3=0,0
                if i<(len(arr1)-1):
                    z2=check_max(arr1,i+1,j)
                if j<(len(arr1[0])-1):
                    z3=check_max(arr1,i,j+1)
                # print('i ',i,' j ',j,' z2 ',z2,' z3 ',z3)
                vis[i][j]= max(z2,z3)
                return vis[i][j]
        return check_max(mat,0,0)
