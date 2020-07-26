# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next  # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head

    def reverse_func_while(self, firstList):
        secondList = []
        counter = len(firstList) - 1
        while counter >= 0:
            secondList.append(firstList[counter])
            counter -= 1
        return secondList


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.reverse_func_while([1, 2, 3]))
    print(Sol.reverseList([1, 2, 3]))
