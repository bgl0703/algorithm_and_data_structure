def climb_stairs(n: int) -> int:
    pre1, cur = 1, 1

    for _ in range(n-1):
        pre1, cur = cur, pre1 + cur
    return cur


if __name__ == '__main__':
    ret = climb_stairs(5)
    print(ret)
