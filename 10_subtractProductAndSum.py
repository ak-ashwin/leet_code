from typing import List


# Example 1:
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
# Example 2:
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = 0
        prod = 1
        sumtotal = 0
        for number in str(n):
            number = int(number)
            prod = prod * number
            sumtotal = sumtotal + number

        res = prod - sumtotal
        return res


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.subtractProductAndSum(234))
    print("done")
