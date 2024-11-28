class Solution:
    def wordBreak(self, s, wordDict):
        length = len(s) 
        pointers = list()
        for word in wordDict:
            if len(word) not in pointers:
                pointers.append(len(word))
        pointers.sort()
        
        dp = [False] * length

        for pointer in pointers:
            if s[:pointer] in wordDict:
                dp[pointer-1] = True

        for i in range(pointers[0], length):
            for pointer in pointers:
                start_index = i - pointer + 1
                if start_index > 0 and dp[start_index-1 ]:
                    substring = s[start_index:i+1]
                    if substring in wordDict:
                        dp[i] = True
                        break

        return dp[-1]
    
string = "abcd"
wordDict = ["a","abc","b","cd"]
s = Solution()
print(s.wordBreak(string,wordDict))



