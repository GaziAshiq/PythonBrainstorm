class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
# source: https://leetcode.com/problems/length-of-last-word
