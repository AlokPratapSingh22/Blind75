"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

1 -> 2 -> 3 -> 4 -> 5

5 <- 4 <- 3 <- 2 <- 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head: Optional[ListNode])-> Optional[ListNode]:
    
    tmp = head
    prev = None

    while tmp:
        nxt = tmp.next
        tmp.next = prev
        prev = tmp
        tmp = nxt
    
    return prev

