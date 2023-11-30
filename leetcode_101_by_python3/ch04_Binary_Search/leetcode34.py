from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        low = self.bin_search_left(nums, left, right, target)
        high = self.bin_search_right(nums, left, right, target)
        if low <= high:
            return [low, high]
        else:
            return [-1, -1]



    def bin_search_left(self, nums: List[int], left: int, right: int, target: int):
        low, high = left, right
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def bin_search_right(self, nums: List[int], left: int, right: int, target: int):
        low, high = left, right
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high


if __name__ == '__main__':
    nums = [5, 7, 7, 9, 9, 10]
    target = 8
    s = Solution()
    s.searchRange(nums, target)