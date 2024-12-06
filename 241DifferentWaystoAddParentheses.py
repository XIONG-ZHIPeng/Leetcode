class Solution:
    def __init__(self):
        self.result = list()
        self.sign = {"*", "+", "-"}

    def diffWaysToCompute(self, expression):
        nums, signify = list(), list()
        num = ""
        for c in expression:
            if c not in self.sign:
                num = num + c
            else:
                nums.append(num)
                num = ""
                signify.append(c)
        else:
            nums.append(num)
            num = ""
            
    
        def rec(nums, signify):
            if len(nums) == 1:
                self.result.append(int(nums[0]))
            else:
                for index, op in enumerate(signify):
                    num1, num2 = nums[index], nums[index+1]
                    new_num = str(eval(num1 + op + num2))
                    rec(nums[:index] + [new_num] + nums[index+2:], signify[:index] + signify[index+1:])
        rec(nums, signify)
        return self.result

s = Solution()
print(s.diffWaysToCompute("2*3-4*5"))