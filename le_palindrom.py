class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit

            x = x // 10
        print(x)
        print(reversed_num)
        if reversed_num != x:
            return False
        else:
            return  True

ob = Solution()
print(ob.isPalindrome(121))