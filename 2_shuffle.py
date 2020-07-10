from typing import List


# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         l1 = nums[:n]
#         l2 = nums[n:]
#
#         output = []
#
#         for i, num in enumerate(l1):
#             output.append(l1[i])
#             output.append(l2[i])
#
#         return output

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = nums[:n]
        l2 = nums[n:]

        output = []

        for i, j in zip(l1, l2):
            output = output + [i, j]

        return output


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.shuffle([2, 5, 1, 3, 4, 7], 3))
