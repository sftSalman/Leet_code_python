class Solution:
    def removeDuplicates(self,nums:list[int])->int:
        left_pointer = 1
        for r  in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[left_pointer] = nums[r]
                left_pointer+=1
        return left_pointer