class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i ** 0.5 % 1 == 0:
                dp[i] = 1
            else:
                dp[i] = 1 + min([dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)])
            # print(f"dp == {dp}")
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.numSquares(13)
    for i in range(1, 5):
        print(int((i ** 0.5) + 1))
