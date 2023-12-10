from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        dp[1] = nums[0]
        for num in nums[1:]:
            flag = True
            for i in range(1, len(dp)+1):
                if num <= dp[i]:
                    dp[i] = num
                    flag = False
                    break
            if flag:
                dp[i+1] = num
        return len(dp)


if __name__ == '__main__':
    nums = [4, 10, 4, 3, 8, 9]
    s = Solution()
    ret = s.lengthOfLIS(nums)
    print(ret)