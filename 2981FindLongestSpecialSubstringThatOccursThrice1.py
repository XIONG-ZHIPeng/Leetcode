class Solution:
    def maximumLength(self, s):
        length = len(s)
        result = -1
        for i in range(1,length-1):
            substring = dict()
            index_range = length - i + 1
            for start in range(index_range):
                new_sub = s[start:start+i]
                if new_sub.count(new_sub[0]) < len(new_sub):
                    continue
                if new_sub not in substring:
                    substring[new_sub] = 1
                else:
                    substring[new_sub] += 1
                    if substring[new_sub] >= 3:
                        result = i if i > result else result
                        del substring
                        break
        return result
        
        
        
        