"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
        BruteForce
        O(kN) time and O(n) space
    """
    def mergeTwoLists(l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            return ListNode(l1.val, mergeTwoLists(l1.next, l2))
        else:
            return ListNode(l2.val, mergeTwoLists(l1, l2.next))

    ans = None

    for lst in lists:
        ans = mergeTwoLists(ans, lst)

    return ans


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Bruteforce using sorting
        O(N logN) time and O(N) space
    """
    nodes = []
    if lists == []:
        return None

    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next

    head = t = ListNode()
    for node in sorted(nodes):
        t.next = ListNode(node)
        t = t.next

    return head.next


def mergeKLists(lists):
    """
    Priority Queue
    O(N logK) time

    :type lists: List[ListNode]
    :rtype: ListNode
    """
    head = point = ListNode(0)
    q = PriorityQueue()
    for l in lists:
        if l:
            q.put((l.val, l))
    while not q.empty():
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, node))
    return head.next


def mergeKLists(self, lists):
    """
    Divide and conquer

    O(N logk) time

    :type lists: List[ListNode]
    :rtype: ListNode
    """

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None
