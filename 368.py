class Solution:
    def largestDivisibleSubset(self, nums):
        length = len(nums)
        if length == 1:
            return [nums[0]]
        nums.sort()
        dp = [1] * length
        subs = [[nums[i]] for i in range(length)]
        for i in range(1,length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] == dp[j] + 1:
                        subs[i] = subs[j] + [nums[i]]
        
        max_index = dp.index(max(dp))
        
        return subs[max_index]
    
s = Solution()
print(s.largestDivisibleSubset([3,4,8,16])) # [1,2]
