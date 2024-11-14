class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict: dict[str:int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result: int = 0
        prev: int = 0
        for i in s:
            curr: int = roman_dict[i]
            if prev < curr:
                result += curr - 2 * prev
            else:
                result += curr
            prev = curr
        return result
print(Solution().romanToInt("IV"))

# Problem link: https://leetcode.com/problems/roman-to-integer/
