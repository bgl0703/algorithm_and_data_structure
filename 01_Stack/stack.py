class Stack:
    def __init__(self, stack_size=None):
        """size==None不对stack大小做限制"""
        self.stack_size = stack_size
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        if self.stack_size is None:
            return False
        else:
            return self.size() == self.stack_size

    def pop(self):
        if self.is_empty():
            raise Exception("the stack is empty")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            raise Exception("the stack is full")
        self.stack.append(value)

    def peek(self):
        if self.is_empty():
            raise Exception("the stack is empty")
        return self.stack[self.size() - 1]

# 进制转换
def decimal_conv(value, deci=2):
    my_stack = Stack()
    ret = ""
    while value > 0:
        rem = value % deci
        my_stack.push(rem)
        value = value // deci
    while not my_stack.is_empty():
        ret += str(my_stack.pop())
    return ret

def exp():
    pass

if __name__ == '__main__':
    a = 8
    result = decimal_conv(8)
    print(result)