from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False

        dp = [False] * nums_sum//2 + 1
        dp[0] = True

        for num in nums:
            for i in range(nums_sum//2, num-1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1]


if __name__ == '__main__':
    for i in range(10, 4, -1):
        print(i)
