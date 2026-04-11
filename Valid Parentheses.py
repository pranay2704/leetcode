class Solution:
    def isValid(self, s: str) -> bool:
        # s=']'
        c = []
        for i in s:
            if i in ['(', '{', '[']:
                c.append(i)
            elif len(c)>0 :
                if ((i==')' and c[-1]!='(') or (i==']' and c[-1]!='[') or(i=='}' and c[-1]!='{')):
                    return False
                else:
                    c.pop()
            else:
                return False
        if len(c)==0:
            return True
        else:
            return False
