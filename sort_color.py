class Solution:
    def isPalindrome(self, x):
       if x[::-1] == x:
           return True
       else :
           return False


ob = Solution()
print(ob.isPalindrome('122'))

