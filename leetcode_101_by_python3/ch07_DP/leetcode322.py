from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins = sorted(coins, reverse=False)
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            # dp[i] = min(dp[i-])
            c_min = []
            for c in coins:
                if i >= c:
                    # print(f"i == {i} == c ==={c}")
                    if dp[i - c] != 0 or i - c == 0:
                        c_min.append(dp[i-c] + 1)
                        dp[i] = min(c_min)
            # print(f"dp==={dp}===i==={i}")

        if dp[-1] == 0:
            return -1
        else:
            return dp[-1]



if __name__ == '__main__':
    coins = [186,419,83,408]
    amount = 6249
    s = Solution()
    ret = s.coinChange(coins, amount)
    print(ret)

