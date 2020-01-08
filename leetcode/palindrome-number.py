# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        if (x < 0) or (x % 10 == 0):
            return False

        reverse = 0
        num = x
        while num > reverse:
            reverse = 10 * reverse + (num % 10)
            num //= 10
        return (num == reverse) or (num == reverse // 10)

    