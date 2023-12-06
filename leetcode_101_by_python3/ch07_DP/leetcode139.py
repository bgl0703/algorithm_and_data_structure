from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        s_len = len(s)
        dp = [False] * s_len
        for i in range(s_len + 1):
            if s[:i] in wordDict:
                dp[i-1] = True
        if True not in dp:
            return False

        for j in range(s_len):
            for k in range(j, s_len+1):
                # print(f"dp[j-1] === {dp[j-1]}====={s[j:k]}")
                if dp[j-1] and s[j:k] in wordDict:
                    dp[k-1] = True
                if dp[-1]:
                    return True
        # print(f"dp======{dp}")

        return dp[-1]



if __name__ == '__main__':
    s = "goalspecial"
    wordDict = ["go","goal","goals","special"]
    So = Solution()
    ret = So.wordBreak(s, wordDict)
    print(ret)