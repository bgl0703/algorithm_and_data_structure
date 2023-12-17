from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set_mums = set(nums)
        res_ = []
        for i in range(1, n+1):
            if i in set_mums:
                continue
            else:
                res_.append(i)
        return res_

if __name__ == '__main__':
    pass