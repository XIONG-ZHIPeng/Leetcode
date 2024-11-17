class Solution:
    def minDistance(self, word1, word2):
        length_word1, length_word2 = len(word1), len(word2)
        dp = [[i if j == 0 else j for i in range(length_word1+1)] for j in range(length_word2+1)]

        for i in range(1,length_word1+1):
            for j in range(1,length_word2+1):
                dp[j][i] = min(dp[j][i-1]+1,  dp[j-1][i]+1)
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = min(dp[j][i], dp[j-1][i-1])
                else:
                    dp[j][i] = min(dp[j][i], dp[j-1][i-1]+1)

        return dp[-1][-1]

word1 = "horse"
word2 = "ros"

s = Solution()
print(s.minDistance(word1,word2))