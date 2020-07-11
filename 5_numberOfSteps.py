from typing import List


# Example 1:
#
# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by  2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

# Example 2:
#
# Input: num = 8
# Output: 4
# Explanation:
# Step 1) 8 is even; divide by 2 and obtain 4.
# Step 2) 4 is even; divide by 2 and obtain 2.
# Step 3) 2 is even; divide by 2 and obtain 1.
# Step 4) 1 is odd; subtract 1 and obtain 0.
# Example 3:
#
# Input: num = 123
# Output: 12

class Solution:
    def numberOfSteps(self, num: int) -> int:

        output = 0

        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            output = output + 1

        return output


# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#         steps = 0
#         while num > 0:
#             """
# 				If number is Even means We Can Do Division in 1 step
# 				However, If it is odd It is 2 steps (1 Subtract and 1 Division)
# 				Beware: For number `1` though just subtract will give you `0` so it is same as divisible by 2 (Just 1 step)
# 			"""
#             if num % 2 == 0 or num == 1:
#                 steps += 1
#             else:
#                 steps += 2
#
#             num = num // 2
#
#         return steps


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.numberOfSteps(14))
