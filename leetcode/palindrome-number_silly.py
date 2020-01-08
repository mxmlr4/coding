# https://leetcode.com/problems/palindrome-number/
# silly but the simpliest single line solution :)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]   

