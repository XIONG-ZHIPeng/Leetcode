class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        previous, current = [0] * n, [0] * n

        previous[0] = grid[0][0]
        for i in range(1,n):
            previous[i] = previous[i-1] + grid[0][i]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    current[j] = previous[j] + grid[i][j]
                else:
                    current[j] = min(previous[j], current[j-1]) + grid[i][j]
            
            previous, current = current, previous

        return previous[-1]