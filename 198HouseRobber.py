class Solution:
    def rob(self, nums) -> int:
        # length = len(nums)
        # dp = [0] * (length + 3)
        # for i in range(length):
        #     dp[i+3] = max(dp[i],dp[i+1]) + nums[i]
        
        # return max(dp[-3:])
        prev1 = 0 
        prev2 = 0 
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2, prev1 = prev1, current
            
        return prev1 