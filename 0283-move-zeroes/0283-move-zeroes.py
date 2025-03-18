class Solution(object):
    def moveZeroes(self, nums):
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeros] = nums[i]
                zeros += 1
        for i in range(zeros, len(nums)):
            nums[i] = 0
