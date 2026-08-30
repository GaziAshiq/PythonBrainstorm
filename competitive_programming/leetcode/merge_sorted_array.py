class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2[:n]
        # nums1.sort()
        print(nums1)



print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
