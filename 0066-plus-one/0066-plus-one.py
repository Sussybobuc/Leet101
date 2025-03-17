class Solution(object):
    def plusOne(self, digits):
        num_str = ''.join(map(str, digits))  
        num = int(num_str) + 1  
        num_str = str(num)  
        if num_str.endswith("0"):  
            return [int(digit) for digit in num_str]          
        return [int(digit) for digit in num_str]  