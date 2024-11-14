class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        output: str = ""
        min_str_len: int = min(len(s) for s in strs)

        for i in range(min_str_len):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                output += char
            else:
                break

        return output


data = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(data))

data = ["flower", "flow", "flight"]

print(Solution().longestCommonPrefix(data))

# problem link: https://leetcode.com/problems/longest-common-prefix/
