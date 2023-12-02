from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = 2
        cnt = 0
        low, high = 0, 2
        while high < len(nums):
            if nums[high] - nums[high-1] == nums[high - 1] - nums[low]:
                length += 1
                cnt += length - 2
            else:
                length = 2
            low += 1
            high = low + 2
        return cnt


if __name__ == '__main__':
    nus = [1, 2, 3, 4, 6, 8]
    s = Solution()
    ret = s.numberOfArithmeticSlices(nus)
    print(ret)
    # ret = number_of_arithmetic_slices(nus)
    # print(ret)
