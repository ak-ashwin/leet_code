from typing import List


# Example 1:
#
# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
# Example 2:
#
# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
# Example 3:
#
# Input: n = 1, start = 7
# Output: 7
# Example 4:
#
# Input: n = 10, start = 5
# Output: 2

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0

        i = 0
        while i < n:
            val = start + 2 * i
            output = val ^ output
            i += 1
        return output



# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         output = 0
#
#         nums = [None] * n
#         for i in range(n):
#             val = start + 2 * i
#             nums[i] = val
#             output = val ^ output
#         print(nums)
#         return output


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.xorOperation(5, 0))
