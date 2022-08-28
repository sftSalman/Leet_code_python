# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x[::-1] == x:
#             return True
#         else:
#             return False
#
# ob = Solution()
# print(ob.isPalindrome(121))


num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    print('first '+ str(reversed_num))
    num = num//10
    print(num)

print("Reversed Number: " + str(reversed_num))