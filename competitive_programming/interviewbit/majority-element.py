class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        counter = {}

        for i in A:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        max = 0
        k = 0
        for key in counter:
            if counter[key] > max:
                max = counter[key]
                k = key
        return k

print(Solution().majorityElement(A = [2, 1, 2]))
print(Solution().majorityElement(A = [1, 2, 2, 3, 3,1,1]))

# problem link: https://www.interviewbit.com/problems/majority-element/