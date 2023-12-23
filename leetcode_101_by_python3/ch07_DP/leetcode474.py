from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]

        for s in strs:
            num_0 = s.count("0")
            num_1 = s.count("1")

            for i in range(m, num_0 - 1, -1):
                for j in range(n, num_1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-num_0][j-num_1] + 1)
        return dp[m][n]



if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3

    solu = Solution()
    ret = solu.findMaxForm(strs, m, n)
    print(ret)