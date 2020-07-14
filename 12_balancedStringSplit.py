from typing import List
from collections import Counter


# Example 1:
#
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:
#
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.


def arr_count_keys(MyList, unique_keys):
    a_list = dict(Counter(MyList))
    l = unique_keys[0]
    r = unique_keys[1]

    if l in a_list:
        l_count = a_list[l]
    else:
        l_count = 0
    if r in a_list:
        r_count = a_list[r]
    else:
        r_count = 0

    return l_count, r_count


def keys_equal(MyList, unique_keys):
    l, r = arr_count_keys(MyList, unique_keys)
    if l == r:
        return True
    else:
        return False


class Solution:
    def balancedStringSplit(self, s: str) -> int:

        s_list = list(s)

        unique_keys = list(set(s_list))
        arr = s_list.copy()
        output = 0
        for i, _ in enumerate(s_list):
            j = i + 1
            if j > 1:
                if keys_equal(arr[:j], unique_keys):
                    output += 1

        return output


# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#
#         scale = 0
#         max_balance = 0
#
#         for c in s:
#
#             if (c == 'R'):
#                 scale += 1
#             else:
#                 scale -= 1
#
#             if (scale == 0):
#                 max_balance += 1
#
#         return max_balance

# class Solution:
#     def balancedStringSplit(self, S: str) -> int:
#         m = c = 0
#         for s in S:
#             if s == 'L': c += 1
#             if s == 'R': c -= 1
#             if c == 0: m += 1
#         return m





if __name__ == "__main__":
    Sol = Solution()
    print(Sol.balancedStringSplit("RLLLLRRRLR"))
    print(Sol.balancedStringSplit("RLRRLLRLRL"))
    print(Sol.balancedStringSplit("LLLLRRRR"))
    print(Sol.balancedStringSplit("RLRRRLLRLL"))


