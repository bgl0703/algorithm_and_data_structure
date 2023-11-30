from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        nums_uniq = list(set(nums))
        nums_uniq_sum = sum(nums_uniq)
        res = nums_sum - 3 * nums_uniq_sum
        return int(-(res/2))


if __name__ == '__main__':
    nums = [0, 1, 0, 1, 0, 1, 99]
    s = Solution()
    res = s.singleNumber(nums)
    print(res)