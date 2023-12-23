from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, res = float("+inf"), 0

        for p in prices:
            cost = min(p, cost)
            res = max(res, p - cost)
        return res



if __name__ == '__main__':
    prices = [3, 2, 6, 5, 0, 3]
    s = Solution()
    ret = s.maxProfit(prices)
    print(ret)