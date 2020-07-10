import operator
from itertools import accumulate
from typing import List


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         output = nums
#         for i, num in enumerate(nums):
#             if i < len(nums) and i != 0:
#                 print(i)
#                 output[i] = nums[i] + nums[i - 1]
#         return output


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         op = accumulate(nums, operator.add)
#         for each in op:
#             print(each)
#         return op

# class Solution:
#     def runningSum(self, nums):
#         i = 1
#         while i < len(nums):
#             nums[i] += nums[i - 1]
#             i += 1
#         return nums

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cum_sum = 0  # cummulative sum
        for i in range(len(nums)):
            cum_sum = cum_sum + nums[i]
            nums[i] = cum_sum
        return nums


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.runningSum([1, 2, 3, 4]))
