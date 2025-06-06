class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        while n > 0:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                break
        return n == 1

        