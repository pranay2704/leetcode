class Solution:
    def minParentheses(self, s):
        # code here 
        st=[]
        i=0
        while len(s)>0:
            if len(st)>0:
                if st[-1]=='(' and s[0]==')':
                    st=st[:-1]
                else:
                    st.append(s[0])
            else:
                st.append(s[0])
            s=s[1:]
        return len(st)
