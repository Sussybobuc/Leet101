class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repp = {}
        for num in nums:
            repp[num] = repp.get(num, 0) + 1  
            if repp[num] == 2:  
                duplicate = num
        for i in range(1, len(nums) + 1):
            if i not in repp: 
                missing = i
        return [duplicate, missing]
