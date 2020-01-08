// https://leetcode.com/problems/string-to-integer-atoi/

class Solution {
public:
    int myAtoi(string str) {
        if(str.empty()) {
            return 0;
        }
        
        auto it = str.cbegin();
        while(*it == ' ') {
            it++;
            if(it == str.cend())
                return 0;
        }
        
        int result = 0;
        bool is_negative = (*it == '-');
        if(*it == '-' || *it == '+') {
            it++;
        }
            
        const int MAX_VALUE_10 = INT_MAX / 10;
        const int MAX_VALUE_LAST_DIGIT = INT_MAX % 10 + (is_negative ? 1 : 0);
        while (it != str.cend() and ('0' <= *it and *it <= '9')) {
            int digit = (*it - '0');
            if (MAX_VALUE_10 < result or (MAX_VALUE_10 == result and MAX_VALUE_LAST_DIGIT <= digit)) {
                return is_negative ? INT_MIN : INT_MAX;
            }
            
            result = 10 * result + digit;
            it++;
        }
        
        return is_negative ? -result : result;
    }
};