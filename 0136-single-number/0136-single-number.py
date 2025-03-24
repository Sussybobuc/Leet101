class Solution(object):
    # def singleNumber(self, nums):
    #     num = {}
    #     for index in nums:
    #         num[index] = num.get(index, 0 ) + 1
    #         if num[index] == 2:
    #             del num[index]
    #         elif num[index] == 1:
    #             single = index
    #     return single
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num 
        return result
