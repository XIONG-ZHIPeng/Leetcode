class Solution:
    def __init__(self):
        self.palindrome = list()

    def partition(self, s):

        def is_palindrome(string):
            length = len(string)
            if length == 1:
                return True
            left, right = 0, length - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def rec(string, substring):
            length = len(string)
            if length == 0:
                self.palindrome.append(substring)
            else:
                for i in range(1,length+1):
                    if is_palindrome(string[:i]):
                        if i < length:
                            rec(string[i:], substring + [string[:i]])
                        else:
                            rec('', substring + [string[:i]])

        rec(s,[])
        return self.palindrome
    
string = "aab"
s = Solution()
s.partition(string)
            
                


        


        