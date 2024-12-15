class Solution:
    def countNumbersWithUniqueDigits(self, n):
        dp = [1] * (n+1)
        if n == 0:
            return sum(dp)
        for i in range(1,n+1):
            result = 1
            if i != 1:
                result *= 9

                for j in range(2,i+1):
                    result *= (11-j)
            else:
                result *= 9
            dp[i] = result
        return sum(dp)
        


        



s= Solution()


print(s.countNumbersWithUniqueDigits()) # 91