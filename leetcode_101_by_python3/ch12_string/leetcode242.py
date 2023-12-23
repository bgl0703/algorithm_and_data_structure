class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_1 = {}
        for char1 in s:
            if char1 in dict_1:
                dict_1[char1] += 1
            else:
                dict_1[char1] = 1

        for char2 in t:
            if char2 in dict_1:
                if dict_1[char2] == 1:
                    dict_1.pop(char2)
                else:
                    dict_1[char2] -= 1
            else:
                return False
        if not dict_1:
            return True
        else:
            return False











if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    dict1 = {"aa": 11, "cc":22, "dd":33}
    dict2 = {"cc": 22, "aa": 11, "dd": 33}



    # solu = Solution()
    # res = solu.isAnagram(s, t)
    # print(res)