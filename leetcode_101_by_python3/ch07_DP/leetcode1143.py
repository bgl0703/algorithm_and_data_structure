class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            # print(f"dp ==== {dp}")
            dp2 = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp2[j] = dp[j - 1] + 1
                else:
                    dp2[j] = max(dp[j], dp2[j - 1])
            dp = dp2

        return dp[n]


if __name__ == '__main__':
    pass