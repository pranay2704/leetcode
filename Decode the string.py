class Solution:
    def decodedString(self, s):
        # code here
        def mul(self,st):
            j=0
            while j<len(st) and st[j]!=']' :
                j+=1
            i=j-1
            while i>=0 and st[i]!='[':
                i-=1
            # print(i,'-',j)
            # print(st[i+1:j])
            if j==len(st) and i==-1:
                # print('s=',st)
                # print(st)
                return st
            else:
                # print('i',i,'-','j',j)
                z1,z2,z3='','',''
                l=i
                while
                
                if i>0:
                    z1=st[:i-1]
                if j<=len(st)-2:
                    z2=st[j+1:]
                if i<j:
                    # print(st[i+1:j+1])
                    z3=(int(st[i-1])*st[i+1:j])
                # print('z1',z1,' z2',z2,' z3',z3)
                z4=z1+z3+z2
                # print('z4=',z4)
                return mul(self,z4)
        z=mul(self,s)
        return z
