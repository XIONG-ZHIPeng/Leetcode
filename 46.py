class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = list()
        if length == 1:
            result.append(nums)
        else:
            for i in range(length):
                for item in self.permute(nums[:i] + nums[i+1:]):
                    result.append([nums[i]] + item)
        return result
            

        
        