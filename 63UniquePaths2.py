class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[1 if obstacleGrid[y][x] == 0 else 0 for x in range(n)] for y in range(m)]
        for i in range(m):
            while dp[i][0] == 0 and i < m-1:
                dp[i+1][0] = 0
                i += 1
        for i in range(n):
            while dp[0][i] == 0 and i < n-1:
                dp[0][i+1] = 0
                i += 1
        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j] == 0:
                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
s = Solution()
print(s.uniquePathsWithObstacles([[1,0]]))