class Solution:
    def wordBreak(self, s, wordDict):
        length = len(s)
        dp, previous = [False] * length, [[] for _ in range(length)]
        pointers = list()
        for word in wordDict:
            if len(word) not in pointers:
                pointers.append(len(word))
        pointers.sort()
        
        for index in range(pointers[0]-1,length):
            for pointer in pointers:
                if index == pointer - 1 or (index - pointer + 1 > 0 and dp[index-pointer]):
                    if s[index-pointer+1:index+1] in wordDict:
                        dp[index]= True
                        previous[index].append(index - pointer)
        
        result = list()
        def find_previous(index_list, string, s, result):

            if not index_list:
                result.append(string[:-1])
            else:
                for index in index_list[-1]:
                    find_previous(index_list[:index + 1], s[index+1:] + ' ' + string, s[:index + 1], result)
        
        if dp[-1]:
            find_previous(previous, '', s, result)

        return result



        


string = "bb"
wordDict = ["a","b","bbb","bbbb"]
s= Solution()


print(s.wordBreak(string, wordDict))