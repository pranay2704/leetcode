class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(sorted(n)))
