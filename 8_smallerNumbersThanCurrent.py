from typing import List


# Example 1:
#
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:
#
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:
#
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]


# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#
#         arr = nums
#         newarr = [0] * len(nums)
#         for k, n in enumerate(nums):
#             for i in arr:
#                 if n > i:
#                     newarr[k] = newarr[k] + 1
#
#         return newarr

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        sorted_list = sorted(nums)

        for i, n in enumerate(sorted_list):
            if n not in dic:
                dic[n] = i
        arr = [dic[n] for n in nums]
        return arr


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print("done")
