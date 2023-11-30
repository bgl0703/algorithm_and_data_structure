"""
回文链表
"""
from typing import Optional


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def reserve(self, start: int, end: int):
        dum = Node(-1)
        dum.next = self.head
        pre = dum
        cur = self.head
        temp = start
        while temp > 0:
            pre = cur
            cur = cur.next
            temp -= 1
        for i in range(end - start):
            cur_next = cur.next
            cur.next = cur.next.next
            cur_next.next = pre.next
            pre.next = cur_next
            # cur = pre.next

    def show(self, h):
        cur = h
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def is_palindrome(self) -> bool:
        slow, fast = self.head, self.head
        start = 0
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            start += 1
        # print(f"start == {start}, fast === {fast}")
        if fast is None:
            self.reserve(start, 2*start - 1)
        else:
            self.reserve(start + 1, 2*start)

        cur = self.head
        print(f"slow == {slow.item}")
        constr = slow.next
        print(f"constr == {constr}")

        while constr is not None:
            print(f"cur == {cur.item}, const=={constr.item}")
            if cur.item != constr.item:
                return False

            cur = cur.next
            constr = constr.next

        return True


if __name__ == '__main__':
    l1 = LinkedList()
    head = [1, 2, 3, 4, 3, 2, 1, 0]
    for i in head:
        l1.add(i)
    # l1.show()
    print("===============")

    ret = l1.is_palindrome()
    print(ret)
