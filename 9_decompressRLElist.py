from typing import List

# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
# Example 2:
#
# Input: nums = [1,1,2,3]
# Output: [1,3,3]


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        newarr = []
        freq = 0
        val = 0
        for k, n in enumerate(nums):
            if (k + 1) % 2 == 0:
                val = n
                for _ in range(freq):
                    newarr.append(val)
            else:
                freq = n

        return newarr


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.decompressRLElist([1, 2, 3, 4]))
    print("done")
