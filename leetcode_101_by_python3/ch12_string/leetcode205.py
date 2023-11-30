class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str_dict = {}
        r_str_dict = {}
        for char1, char2 in zip(s, t):
            if char1 not in str_dict and char2 not in r_str_dict:
                str_dict[char1] = char2
                r_str_dict[char2] = char1
            elif char1 in str_dict and char2 in r_str_dict:
                if str_dict[char1] != char2:
                    return False
            else:
                return False

        return True






if __name__ == '__main__':
    s = "badc"
    t = "baba"