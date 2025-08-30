class Solution:
    def celebrity(self, mat):
        # code here
        # print(type(mat))
        res1=[]
        res1 = [0]*len(mat[0])
        res2=res1.copy()
        # print(res)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i!=j and mat[i][j]==1:
                    res1[i]=res1[i]+1
                if mat[i][j]==1:
                    res2[j]=res2[j]+1
                    # print(i,'-',j,'-',res)
                # print('1')
        # print(res1,res2)
        # print(res1.index(0),'-',res2[res1.index(0)])
        try :
            if res1.index(0) != None :
                if res2[res1.index(0)]==len(res1):
                    return res1.index(0)
                else:
                    return -1
            else:
                return -1
        except:
            return -1
 
