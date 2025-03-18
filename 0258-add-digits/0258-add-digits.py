class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num_str = str(num)
            num = sum(int(digit) for digit in num_str)
        return num
        
        