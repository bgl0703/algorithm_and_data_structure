class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if is_primes[i] == 1:
                is_primes[i * i: n: i] = [0] * len(is_primes[i * i: n: i])
        return sum(is_primes)











if __name__ == '__main__':
    s = Solution()
    # s.countPrimes(10)
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list1[3:8:2])
