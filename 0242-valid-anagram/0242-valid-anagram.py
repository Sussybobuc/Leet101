class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
        # s_words = {}
        # t_words = {}
        # for char in s:
        #     s_words[char] = s_words.get(char, 0) + 1
        # for char in t:
        #     t_words[char] = t_words.get(char, 0) + 1
        # return s_words == t_words