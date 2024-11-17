class Solution:
    def jump(self, nums):
        length = len(nums)
        # dp store the min steps to the element
        dp = [float('inf')] * length
        dp[0] = 0

        for index, i in enumerate(nums):
            if i == 0:
                continue
            for j in range(1,min(i+1, length-index)):
                new_step = dp[index] + 1
                if index+j < length and dp[index+j] > new_step:
                    dp[index+j] = new_step
        return dp[-1]
    
    def jump2(self, nums):
        length = len(nums)

        res = 0
        l, r = 0, 0

        while r < length - 1:
            res += 1
            max_r = r
            for i in range(l, r+1):
                max_r = max(max_r, i + nums[i])
            l = r + 1
            r = max_r
        return res
        