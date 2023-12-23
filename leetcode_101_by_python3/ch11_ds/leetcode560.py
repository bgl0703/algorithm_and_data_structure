from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        sums, res = 0, 0
        for num in nums:
            sums += num
            res += dic.get(sums - k, 0)
            dic[sums] = dic.get(sums, 0) + 1
        return res






if __name__ == '__main__':
    nums = [-1, -1, 1]
    k = 0
    s = Solution()
    ret = s.subarraySum(nums, k)
    print(ret)
    # list1 = [0,1,2,3,0]
    # a = list1.count(5)
    # print(a)
    pass