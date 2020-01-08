# https://leetcode.com/problems/longest-palindromic-substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_to_palindrom(s, l, r):
            while 0 <= l and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return l + 1, r - l - 1 # start, length
            

        largest = (0, 0)
        for i in range(len(s)):
            current = expand_to_palindrom(s, i, i)
            if (current[1] > largest[1]):
                largest = current
            current = expand_to_palindrom(s, i-1, i)
            if (current[1] > largest[1]):
                largest = current
        
        return s[largest[0]: largest[0] + largest[1]]