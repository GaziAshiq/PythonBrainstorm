class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a: str = a[::-1]
        b: str = b[::-1]
        output: str = ''
        a_len: int = len(a)
        b_len: int = len(b)
        carry: bool = False


print(Solution().addBinary(a="11", b="1"))
print(Solution().addBinary(a="1010", b="1011"))

# output: list[int] = []
#         a: list[int] = [int(i) for i in a][::-1]
#         b: list[int] = [int(i) for i in b][::-1]
#         a_len = len(a)
#         b_len = len(b)
#         flag: bool = False
#         print(a)
#         print(b)
#
#         if b_len <= a_len:
#             for i in range(a_len):
#                 if b[i] + a[i] != 2:
#                     output.append(b[i] + a[i])
#                 elif b[i] + a[i] == 2:
#                     output.append(0)
#                     flag = True
