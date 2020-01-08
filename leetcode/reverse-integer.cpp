// https://leetcode.com/problems/reverse-integer

#include <limits.h>

class Solution {
public:
    int reverse(int x) {
        if (x == INT_MIN) {
            return 0;
        }

        bool negative = x < 0;
        if (negative) {
            x = -x;
        }

        int r = 0;
        while(x > 0) {
            if (r > (INT_MAX / 10)) {   // No need to check r == (INT_MAX / 10) case.
                                        // In "our environment" first digit of x in this case could be 2 or less and can't cause overflow
                return 0;
            }
            r = r * 10 + x % 10;
            x /= 10;
        }

        return negative ? -r : r;
    }
};