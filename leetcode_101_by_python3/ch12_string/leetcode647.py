class Solution:
    def countSubstrings(self, s: str) -> int:

        cnt = 0
        for i in range(len(s)):
            cnt += self.extend(s, i, i, len(s))
            cnt += self.extend(s, i, i + 1, len(s))
        return cnt

    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res



if __name__ == '__main__':
    s = Solution()
    str1 = "aa"
    ret = s.countSubstrings(str1)
    print(ret)