class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)
        for i in range(haystack_len):
            if needle in haystack[i: needle_len]:
                needle_len += 1
                return i
            needle_len += 1
        return -1

# source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
