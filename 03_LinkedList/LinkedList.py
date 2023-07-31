class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def insert(self, index, item):
        node = Node(item)
        cnt = 0
        pre = None
        cur = self.head
        if self.length() < index:
            raise Exception(f"the linked list length is {self.length()}, and the position to be inserted does not exist")
        while cur is not None:
            if cnt == index:
                break
            pre = cur
            cur = cur.next
            cnt += 1
        if pre is None:
            node.next = self.head
            self.head = node
        else:
            node.next = cur
            pre.next = node

    def append(self, item):
        """向链表尾部添加数据"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def remove(self, item):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                break
            pre = cur
            cur = cur.next
        if cur is None:
            raise Exception(f"{item} is not in the linked list")
        else:
            pre.next = cur.next

    def travers(self):
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def find(self, item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return cur
        return None


if __name__ == '__main__':
    sl = SingleLinkedList()
    sl.append("a")
    sl.append(22)
    sl.insert(1, "wawa")
    sl.travers()
    sl.remove(22)
    print("================")
    sl.travers()
