from typing import List


def number_of_arithmetic_slices(nums: List[int]) -> int:
    nums_len = len(nums)
    if nums_len <= 2:
        return 0
    cnt = 0
    d, t = nums[1] - nums[0], 0

    for i in range(2, nums_len):
        if nums[i] - nums[i-1] == d:
            t += 1
        else:
            t = 0
            d = nums[i] - nums[i-1]
        cnt += t
    return cnt


if __name__ == '__main__':
    nus = [1, 2, 3, 4]
    ret = number_of_arithmetic_slices(nus)
    print(ret)
