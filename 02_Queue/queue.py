class Queue:
    def __init__(self, queue_len=None):
        self.queue_len = queue_len
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        if self.queue_len is None:
            return False
        else:
            return self.size() == self.queue_len

    def enqueue(self, value):
        if self.is_full():
            raise Exception("the queue is full")
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("the queue is empty")
        return self.queue.pop(0)


if __name__ == '__main__':
    my_q = Queue()
    my_q.enqueue(1)
    my_q.enqueue(2)
    ret = my_q.dequeue()
    print(ret)

