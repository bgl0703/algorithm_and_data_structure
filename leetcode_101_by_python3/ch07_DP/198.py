from typing import List


def rob(nums: List[int]) -> int:
    """
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    """
    nums_len = len(nums)
    if nums_len <= 2:
        return max(nums)
    dp = [0] * nums_len
    pre_1, pre_2, cur = max(nums[:2]), nums[0], 0

    for i in range(2, nums_len):
        cur = max(pre_1, pre_2 + nums[i])
        pre_2, pre_1 = pre_1, cur
    return cur




if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    ret = rob(nums)
    print(ret)
