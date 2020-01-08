# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:    
    def myAtoi(self, s: str) -> int:
        INT_MAX  = (1 << 31) - 1
        INT_MIN  = -(1 << 31)

        if s == "":
            return 0
        
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
            
        if i == len(s):
            return 0
        
        result = 0
        is_negative = (s[i] == '-')
        if s[i] in ('-', '+'):
            i += 1
            
        MAX_VALUE_10 = INT_MAX // 10
        MAX_VALUE_LAST_DIGIT = INT_MAX % 10 + (1 if is_negative else 0)
        while i < len(s) and ('0' <= s[i] and s[i] <= '9'):
            digit = int(s[i])
            if (MAX_VALUE_10 < result or (MAX_VALUE_10 == result and MAX_VALUE_LAST_DIGIT <= digit)):
                return INT_MIN if is_negative else INT_MAX
            
            result = 10 * result + digit
            i += 1
        
        return -result if is_negative else result

