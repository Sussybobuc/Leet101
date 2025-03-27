class Solution(object):
    def hammingWeight(self, n):
        binary = bin(n)[2:]
        one = '1'
        return binary.count(one)