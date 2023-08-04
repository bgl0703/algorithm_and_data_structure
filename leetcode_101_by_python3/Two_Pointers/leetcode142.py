from typing import Optional


class ListNode:
    def __init__(self, item):
        self.value = item
        self.next = None


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, head = head, head
    while True:
        if not (fast and fast.next):
            return
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            break
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast