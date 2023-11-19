class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        size = len(nums)
        self.target = target
        two_index = []

        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] + nums[j] == target:
                    two_index.append(i)
                    two_index.append(j)
                    return two_index


solution = Solution()
print(solution.twoSum(nums=[2, 5, 5, 11], target=7))
