import math
class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        nums = [0] * n
        nums[0], nums[1] = 1, 1
        for index in range(2, int(math.sqrt(n)) + 1):
            if nums[index]:
                continue
            else:
                next_index = index * index
                while next_index < n:
                    nums[next_index] = 1
                    next_index += index
        
        return nums.count(0)






        