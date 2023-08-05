def judge_square_sum(c: int) -> bool:

    nums_list = list(range(int(pow(c, 0.5)) + 1))
    left, right = 0, len(nums_list) - 1
    while left <= right:
        a = pow(nums_list[left], 2)
        b = pow(nums_list[right], 2)
        if a + b == c:
            return True
        if a + b < c:
            left += 1
        if a + b > c:
            right -= 1
    return False


if __name__ == '__main__':
    ret = judge_square_sum(9)
    print(ret)