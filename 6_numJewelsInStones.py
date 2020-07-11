from typing import List


# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
# Note:
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        output = 0
        for stone in S:
            for jewel in J:
                if jewel == stone:
                    output = output + 1
        return output





if __name__ == "__main__":
    Sol = Solution()
    print(Sol.numJewelsInStones("aA", "aAAbbbb"))
