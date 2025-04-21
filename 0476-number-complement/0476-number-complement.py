class Solution(object):
    def findComplement(self, num):
        x = bin(num)[2:]
        complement = ''.join(['0' if b == '1' else '1' for b in x])
        return int(complement, 2)
        