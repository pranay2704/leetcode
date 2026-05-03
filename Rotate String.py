class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        if n!=len(goal):
            return False
        s=s+s
        for i in range(n):
            if s[i:i+n]==goal:
                return True
        return False
