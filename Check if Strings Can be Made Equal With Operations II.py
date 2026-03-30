class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        lt1,lt2,rt1,rt2 = [],[],[],[]
        for i in range(len(s1)):
            if i%2==0:
                lt1.append(s1[i])
                lt2.append(s2[i])
            else:
                rt1.append(s1[i])
                rt2.append(s2[i])
        if sorted(lt1)!=sorted(lt2) or sorted(rt1)!=sorted(rt2):
            return False
        return True
