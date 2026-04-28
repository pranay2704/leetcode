class Solution:
    def minOperations(self, grid, x):
        m, n = len(grid), len(grid[0])
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])

        # Check if all have same remainder modulo x
        r = arr[0] % x
        for a in arr:
            if a % x != r:
                return -1

        # Sort and pick median
        arr.sort()
        target = arr[len(arr) // 2]

        # Count operations
        total_ops = 0
        for v in arr:
            total_ops += abs(v - target) // x

        return total_ops
