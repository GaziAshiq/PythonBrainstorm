class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        output: list[list[int]] = [[0,0]]


        """
        [[1,3],
        [2,6],
        [8,10],
        [15,18]]
        """
        return output



print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
