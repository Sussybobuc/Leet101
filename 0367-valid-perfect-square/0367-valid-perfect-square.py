import math
class Solution(object):
    def isPerfectSquare(self, num):
        sqrt = math.sqrt(num)
        if sqrt % 1 == 0:
            return True
        return False