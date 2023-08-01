from collections import OrderedDict


def cache(func):
    """先引入一个简单的装饰器缓存，其实原理很简单，就是内部用一个字典缓存已经计算过的结果"""
    store = {}

    def _(n):
        if n in store:
            return store[n]
        else:
            res = func(n)
            store[n] = res
            return res
    return _


@cache
def fib(n: int):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


class LRUCache:
    def __init__(self):
        self.od = OrderedDict()
        pass

    def get(self):
        pass

    def update(self):
        pass


if __name__ == '__main__':
    a = fib(8)
    print(a)