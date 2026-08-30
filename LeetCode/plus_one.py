## Best solution
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        output: list[int] = digits[::-1]
        output_len: int = len(output)
        flag: bool = True

        for i in range(output_len):
            if output[i] + 1 == 10:
                output[i] = 0
                flag = True
            elif flag:
                output[i] += 1
                flag = False
                break
        if flag:
            output.append(1)

        return output[::-1]


## fail solution
# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         output: list[int] = []
#         digits_len = len(digits)
#         flag: bool = False
#
#         if digits_len == 1:
#             if digits[0] + 1 == 10:
#                 output.extend([1, 0])
#                 return output
#             else:
#                 output.append(digits[0] + 1)
#                 return output
#         else:
#             i:int = digits_len - 1
#             output.extend(digits)
#             while digits[i] + 1 == 10 and i != -1:
#                 output[i] = 0
#                 i -= 1
#             output[i] += 1
#             return output


## fail solution 2
# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         output: list[int] = []
#         flag: bool = False
#         digits_len = len(digits) - 1
#         # print(digits_len)
#
#         # while digits_len != -1:
#         # if digits[digits_len] + 1 == 10:
#         if digits_len != -1:
#             if digits[digits_len] + 1 == 10:
#                 while digits[digits_len] + 1 == 10 and digits_len != -1:
#                     output.append(0)
#                     digits_len -= 1
#                     flag = True
#             else:
#                 output.append(digits[digits_len] + 1)
#                 digits_len -= 1
#                 flag = False
#         if flag:
#             output.append(1)
#         return output[::-1]


print(Solution().plusOne([9]))
print(Solution().plusOne([0]))
print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([7, 8, 9]))
print(Solution().plusOne([9, 9]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

# source: https://leetcode.com/problems/plus-one
