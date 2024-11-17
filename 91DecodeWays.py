class Solution:
    def numDecodings(self, s):
        
        if not s or s[0] == '0':
            return 0

        length = len(s)
        dp = [0] * (length+1)
        dp[0], dp[1] = 1, 1 

        for i in range(2,length+1):
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]
            if int(s[i-2:i]) > 9 and int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
        
        return dp[-1]
    
s = Solution()
print(s.numDecodings('226'))