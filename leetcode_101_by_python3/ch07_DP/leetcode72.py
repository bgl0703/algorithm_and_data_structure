class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1, len_word2 = len(word1)+1, len(word2)+1
        dp = [[0] * len_word2 for _ in range(len_word1)]
        for i in range(len_word1):
            for j in range(len_word2):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    # i, j = i-1, j-1
                    if word1[i-1] == word2[j-1]:
                        add_num = 0
                    else:
                        add_num = 1
                    dp[i][j] = min(dp[i-1][j-1]+add_num, min(dp[i-1][j] + 1, dp[i][j-1]+1))
            # print(f"dp === {dp}")
        return dp[len_word1-1][len_word2-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    # print(word2[])
    s = Solution()
    ret = s.minDistance(word1, word2)
    print(ret)

