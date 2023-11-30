from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        mid = self.bin_search_k(nums, 0, len(nums) - 1)

        return self.bin_search(nums, 0, mid, target) or self.bin_search(nums, mid+1, len(nums) - 1, target)

    def bin_search_k(self, nums: List[int], left: int, right: int):
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= nums[right] and nums[mid] >= nums[left]:
                return mid

            if nums[mid] <= nums[min(mid+1, len(nums) - 1)] and nums[mid] <= nums[max(mid-1, 0)]:
                return mid - 1
            if nums[mid] < nums[right]:
                right = mid - 1
            if nums[mid] > nums[left]:
                left = mid + 1

    def bin_search(self, nums: List[int], left: int, right: int, target: int):
        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return False








if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    s = Solution()
    res = s.search(nums, target)
    print(res)