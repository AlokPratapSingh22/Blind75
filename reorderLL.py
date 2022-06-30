def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    l = []
    t = head
    while t:
        l.append(t)        
        t = t.next
    
    t = head        
    
    while t and t.next:                
        tail = l.pop()
        l[-1].next = None
        tail.next = t.next
        t.next = tail            
        t = t.next.next
        
    return head