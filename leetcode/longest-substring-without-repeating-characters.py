# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_chars = set()
        max_substring_length = 0
        i = j = 0
        while j < len(s):
            if s[j] not in substring_chars:
                substring_chars.add(s[j])
                j += 1
            else:
                max_substring_length = max(max_substring_length, j - i)
                while i < j:
                    substring_chars.remove(s[i])
                    i += 1
                    if s[i-1] == s[j]:
                        break

        return max(max_substring_length, j - i)

    