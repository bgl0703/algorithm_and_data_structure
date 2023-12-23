class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 2
        if n == 3:
            return 3
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        temp = 1
        cnt = 1
        while True:
            j = n

            while j > 0:
                print(f"tmep == {temp}")
                if dp[j] != 0 and n % j == 0 and j != 1:

                    dp[temp+j] = dp[temp] + 2
                    temp += j
                    break
                if j == 1:
                    dp[temp+1] = dp[temp] + 1
                    temp += 1

                j -= 1
                print(f"j=={j}")
            if dp[n]:
                break

            print(f"dp == {dp}")
        return dp[n]

if __name__ == '__main__':
    n = 9
    s = Solution()
    ret = s.minSteps(n)
    print(ret)
