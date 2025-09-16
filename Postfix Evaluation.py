class Solution:
    def evaluatePostfix(self, arr):
        # code here
        lis=[]
        for i in arr:
            if i not in ('*',"^",'-','+','/'):
                lis.append(int(i))
            elif i=='*':
                z=lis[-2]*lis[-1]
                lis=lis[:-2]
                lis.append(z)
            elif i=='^':
                z=lis[-2]**lis[-1]
                lis=lis[:-2]
                lis.append(z)
            elif i=='-':
                z=lis[-2]-lis[-1]
                lis=lis[:-2]
                lis.append(z)
            elif i=='+':
                z=lis[-2]+lis[-1]
                lis=lis[:-2]
                lis.append(z)
            elif i=='/':
                z=lis[-2]//lis[-1]
                lis=lis[:-2]
                lis.append(z)
        # print(lis)
        return lis[0]
