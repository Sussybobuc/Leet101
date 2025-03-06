class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False  
        s = str(x)  
        n = len(s)
        left_half = s[:n // 2]
        right_half = s[-(n // 2):][::-1]  
        return s.startswith(right_half)
  # i did not use normal method to solve this algorithm, i use the startwith() to compare both side and manually throw out the middle number of odds index. Pretty cool right?
