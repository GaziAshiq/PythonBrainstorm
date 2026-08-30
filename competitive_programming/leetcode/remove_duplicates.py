# initial solution
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         output:list[int] = []
#         for i in range(len(nums)):
#             if nums[i] in output:
#                 continue
#             else:
#                 output.append(nums[i])
#         nums[:len(output)] = output
#         nums[len(output):] = [0]
#         print(nums)
#         print(output)
#         return len(output)

# best solution
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        _nums_len: int = len(nums)
        j: int = 1

        for i in range(1, _nums_len):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[j] = nums[i]
                j += 1
        print(j)
        print(nums)
        return j


# print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([]))
# print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
#                                    `              i
#                                        j
# source: https://leetcode.com/problems/remove-duplicates-from-sorted-array

