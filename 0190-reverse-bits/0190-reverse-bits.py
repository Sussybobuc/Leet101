class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = bin(n)[2:].zfill(32)  
        reversed_num = num[::-1]  
        return int(reversed_num, 2) 