class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_char = {}
        for char in s:
            if char in dict_char:
                dict_char[char] += 1
            else:
                dict_char[char] = 1

        for char in t:
            if char not in dict_char:
                return False

            if char in dict_char:
                dict_char[char] -= 1
                if dict_char[char] == 0:
                    dict_char.pop(char)
        # print(f"dd === {dict_char}")

        if not dict_char:
            return True
        else:
            return False





if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solu = Solution()
    res = solu.isAnagram(s, t)
    print(res)