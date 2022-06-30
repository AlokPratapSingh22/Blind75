"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val < l2.val:
        return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
    else:
        return ListNode(l2.val, self.mergeTwoLists(l1, l2.next))