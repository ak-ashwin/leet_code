from typing import List
from collections import Counter


# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, L, R):
        l = []
        r = []
        ans = 0
        for stack in root:
            if stack != None or stack != "null":
                if stack is not None:
                    if L <= stack <= R:
                        ans += stack
                    if L < stack:
                        l.append(stack)

                    if stack < R:
                        r.append(stack)
        print(str(l) + " :: " + str(r))
        return ans



if __name__ == "__main__":
    Sol = Solution()
    print(Sol.rangeSumBST([10, 5, 15, 3, 7, 0, 18], L=7, R=15))
