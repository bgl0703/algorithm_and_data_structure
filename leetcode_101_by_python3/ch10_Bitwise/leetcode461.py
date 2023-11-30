class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        diff = bin(diff)
        res = diff.count("1")
        return res



if __name__ == '__main__':
    x = 1
    y = 4
    s = Solution()
    s.hammingDistance(x, y)