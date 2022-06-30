class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: Optional[ListNone]) -> bool:
    """Taking a look-up"""
    lst = []
    tmp = head

    while tmp:
        if tmp in lst:
            return True
        else:
            lst.append(tmp)
        tmp = tmp.next

    return False
    
def hasCycle(head: Optional[ListNode]) -> bool:
    """Tortoise Hare"""
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False