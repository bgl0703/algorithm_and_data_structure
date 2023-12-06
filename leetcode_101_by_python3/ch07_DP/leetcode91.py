class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        s = ' ' + s
        dp = [0] * 3
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i % 3] = 0
            a = ord(s[i]) - ord('0')
            b = (ord(s[i - 1]) - ord('0')) * 10 + ord(s[i]) - ord('0')
            if 1 <= a <= 9:
                dp[i % 3] = dp[(i - 1) % 3]
            if 10 <= b <= 26:
                dp[i % 3] += dp[(i - 2) % 3]
        return dp[n % 3]


if __name__ == '__main__':
    s = "2101"
    print(s[:-1])
    # solution = Solution()
    # ret = solution.numDecodings(s)
    # print(ret)

