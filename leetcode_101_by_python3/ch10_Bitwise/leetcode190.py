class Solution:
    def reverseBits(self, n: int) -> int:
        for _ in range(3):
            print(f"n == {n}")
            print(f"bin=={bin(n)}")
            n = n >> 1
            print(f"n>> === {n}")
            print(f"bin__n == {bin(n)}")

if __name__ == '__main__':
    s = Solution()
    s.reverseBits(8)
