class Solution:
    def rob(self, nums) -> int:
        length = len(nums)
        dp = [0] * (length + 3)
        for i in range(length):
            dp[i+3] = max(dp[i],dp[i+1]) + nums[i]
        
        return max(dp[-3:])