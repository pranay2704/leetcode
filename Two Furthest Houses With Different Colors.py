class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        # From left end
        left_max = 0
        for j in range(n-1, -1, -1):
            if colors[0] != colors[j]:
                left_max = j
                break
        # From right end
        right_max = 0
        for i in range(n):
            if colors[n-1] != colors[i]:
                right_max = n - 1 - i
                break
        return max(left_max, right_max)
