from typing import List
from collections import Counter


# Example
# 1:
#
# Input: head = [1, 0, 1]
# Output: 5
# Explanation: (101) in base
# 2 = (5) in base
# 10
# Example
# 2:
#
# Input: head = [0]
# Output: 0
# Example
# 3:
#
# Input: head = [1]
# Output: 1
# Example
# 4:
#
# Input: head = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# Output: 18880
# Example
# 5:
#
# Input: head = [0, 0]
# Output: 0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def reverse_func(text):
#     result = []
#     for i in range(len(text) - 1, -1, -1):
#         result.append(text[i])
#     return result
#
#
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         head = reverse_func(head)
#         sum = 0
#         for i, k in enumerate(head):
#             val = k * (2 ** i)
#             sum = sum + val
#         return sum


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head:
            answer = 2 * answer + head.val
            head = head.next
        return answer


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.getDecimalValue([1, 0, 1]))
    # print(Sol.getDecimalValue([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]))
