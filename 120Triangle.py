import copy
class Solution:
    def minimumTotal(self, triangle):
        length = len(triangle)
        if length == 1:
            return triangle[0][0]
        
        dp = [triangle[0][0]]
        for i in range(1,length):
            current = copy.deepcopy(triangle[i])
            for j in range(i+1):
                if (j-1) > -1 and j < i:
                    current[j] = min(dp[j-1],dp[j]) + current[j]
                elif j == 0:
                    current[j] = dp[j] + current[j]
                else:
                    current[j] = dp[j-1] + current[j]
            
            del dp
            dp = copy.deepcopy(current)
            del current
        
        return min(dp)


        