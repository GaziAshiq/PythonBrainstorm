class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        output: list[int] = []
        for i in nums:
            if i != val:
                output.append(i)
        output_len: int = len(output)
        nums[:output_len] = output

        return output_len

# source: https://leetcode.com/problems/remove-element/