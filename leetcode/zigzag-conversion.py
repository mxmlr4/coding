# https://leetcode.com/problems/zigzag-conversion/
# accumulate result in strings for each row and finally join them


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [""] * numRows
        row_index = 0
        inc = 1
        for c in s:
            rows[row_index] += c
            row_index += inc
            if row_index < 0 or numRows <= row_index:
                row_index -= 2 * inc
                inc = -inc
                
        return "".join(rows)

    
