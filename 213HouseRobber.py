class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        def subrob(nums):
            pre1, pre2 = 0, 0
            for num in nums:
                current = max(pre1, pre2 + num)
                pre1, pre2 = current, pre1
            
            return pre1

        return max(subrob(nums[:-1]), subrob(nums[1:]))