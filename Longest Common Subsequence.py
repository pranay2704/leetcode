class Solution:

    def rec(self,dp,i,j, text1, text2):
        if i>=len(text1) or j>=len(text2):
            return 0
        ans = 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if text1[i] == text2[j]:
            ans = 1+(self.rec(dp,i+1, j+1, text1, text2))
        else:
            ans = max(self.rec(dp,i+1, j, text1, text2), self.rec(dp,i, j+1, text1, text2))
            dp[i][j] = ans
        return ans

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp =[[-1 for _ in range(len(text2)) ] for _ in range(len(text1)) ]
        # print(dp)
        return self.rec(dp,0, 0, text1, text2)
