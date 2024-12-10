# class Solution:
#     def maximumLength(self, s):
#         length = len(s)
#         result = -1
#         for i in range(1,length-1):
#             substring = dict()
#             index_range = length - i + 1
#             for start in range(index_range):
#                 new_sub = s[start:start+i]
#                 if new_sub.count(new_sub[0]) < len(new_sub):
#                     continue
#                 if new_sub not in substring:
#                     substring[new_sub] = 1
#                 else:
#                     substring[new_sub] += 1
#                     if substring[new_sub] >= 3:
#                         result = i if i > result else result
#                         del substring
#                         break
#         return result
        
        
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        l, r = 1, n

        if not self.helper(s, n, l):
            return -1

        while l + 1 < r:
            mid = (l + r) // 2
            if self.helper(s, n, mid):
                l = mid
            else:
                r = mid

        return l

    def helper(self, s: str, n: int, x: int) -> bool:
        cnt = [0] * 26
        p = 0

        for i in range(n):
            while s[p] != s[i]:
                p += 1
            if i - p + 1 >= x:
                cnt[ord(s[i]) - ord('a')] += 1
            if cnt[ord(s[i]) - ord('a')] > 2:
                return True

        return False
    
s = Solution()
print(s.maximumLength("cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"))
        