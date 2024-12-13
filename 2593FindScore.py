class Solution:
    def findScore(self, nums: List[int]) -> int:
        result = 0
        unmark = [(val, index) for index, val in enumerate(nums)]
        unmark.sort()

        marked = [False] * len(nums)
        for item in unmark:
            if marked[item[1]]:
                continue
            marked[item[1]] = True
            result += nums[item[1]]
            if item[1] > 0: marked[item[1] - 1] = True
            if item[1] + 1 < len(nums): marked[item[1] + 1] = True
        return result