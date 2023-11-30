

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        n_2 = bin(n)
        res = n_2.count("1") == 1 and n_2.count("0") % 2 == 1
        return res






if __name__ == '__main__':
    s = Solution()
    res = s.isPowerOfFour(0)
    print(res)
    pass