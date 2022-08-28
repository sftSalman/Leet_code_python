class Solution:
    def isPalindrome(self,x):
        x = str(x)
        if x == x.__reversed__():
            return True
        else:
            return False

s = Solution()
s.isPalindrome(121)