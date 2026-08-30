class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums_len = len(nums)
        if target > nums[nums_len - 1]:
            return nums_len
        elif target <= nums[0]:
            return 0
        else:
            for i in range(1, nums_len):
                if target == nums[i]:
                    return i
                elif nums[i - 1] < target < nums[i]:
                    return i
# -1 3 5 6
#   i

print(Solution().searchInsert([-1, 3, 5, 6], 0))

# source: https://leetcode.com/problems/search-insert-position