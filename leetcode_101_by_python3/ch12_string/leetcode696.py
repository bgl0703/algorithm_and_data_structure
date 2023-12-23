class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre_char_len, cur_char_len = 0, 1
        cnt = 0
        for i, char in enumerate(s):

            if i != 0 and char == s[i-1]:
                cur_char_len += 1
            elif i != 0 and char != s[i-1]:
                pre_char_len = cur_char_len
                cur_char_len = 1
            if cur_char_len <= pre_char_len:
                cnt += 1
            # print(f"i=={i}, char == {char}, pre == ={pre_char_len}, cur === {cur_char_len}, cnt=={cnt}")
        return cnt



if __name__ == '__main__':
    s = "00110011"
    solu = Solution()
    ret = solu.countBinarySubstrings(s)
    print(ret)