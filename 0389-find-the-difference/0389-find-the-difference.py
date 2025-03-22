class Solution(object):
    def findTheDifference(self, s, t):
        words = {}
        for char in s:
            words[char] = words.get(char, 0) + 1
        for char in t:
            words[char] = words.get(char, 0) - 1
            if words[char] == 0:
                del words[char]
        return join(words.keys())
