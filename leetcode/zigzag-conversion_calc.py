# https://leetcode.com/problems/zigzag-conversion/
# append symbol to the result string calculating its position in the input string


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = ""
        step = 2 * numRows - 2
        for i in range(numRows):
            j = i
            while j < len(s):
                result += s[j]                
                if 0 < i and i < (numRows - 1) and (j + step - 2 * i) < len(s):
                    result += s[j + step - 2 * i]                                    
                j += step
        
        return result

    