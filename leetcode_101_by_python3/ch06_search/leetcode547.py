from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ret = 0
        N = len(isConnected)
        for i in range(N):
            print(f"ret==---{ret}")
            ret = max(self.dfs(i, N, isConnected), ret)
        return ret

    def dfs(self, start: int, N: int, isConnected: List[List[int]]):
        if start >= N:
            return 0
        cnt = 1
        for s in range(start+1, N):
            print(f"start=={start}, s == {s} ==== isC == {isConnected[start][s]}")
            if isConnected[start][s] == 1:
                # cnt += 1
                print(f"cnt---bf === {cnt}")
                cnt += self.dfs(s, N, isConnected)
                print(f"cnt---af === {cnt}")
        return cnt


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    s = Solution()
    ret = s.findCircleNum(isConnected)
    print(f"ret === {ret}")