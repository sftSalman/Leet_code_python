class Solution:
    def twoSum(self,nums,target):
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))