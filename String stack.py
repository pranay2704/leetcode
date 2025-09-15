class Solution:
    def stringStack(self, pat, tar):
        # code here
        j=0
        i=0
        s=''
        while j<len(pat):
            if i<len(tar) :
                if tar[i]==pat[j]:
                    if len(s)==0:
                        s+=pat[j]
                        i+=1
                    elif len(s)>0 and s==tar[:i-1]:
                        print(tar[:i-1])
                        s+=pat[j]
                        i+=1
                    elif len(s)>0 and s!=tar[:i-1]:
                        print(tar[:i-1])
                        s=s[:-1]
                elif len(s)>0:
                    if s==tar[:i-1]:
                        s+=pat[j]
                    else:
                        s=s[:-1]
                    # print(s)
                
            elif len(s)>0:
                if s==tar[:i-1]:
                    s+=pat[j]
                else:
                    s=s[:-1]
            print(j,'-',pat[j],'-',s)
            j+=1
        # print(s,'-',tar)
        if s==tar:
            return True
        return False
