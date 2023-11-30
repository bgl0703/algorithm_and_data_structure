from typing import List


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         count_dict = {}
#         for num in nums:
#             if num in count_dict:
#                 a = count_dict.pop(num)
#                 print(a)
#             else:
#                 count_dict[num] = 1
#         # res = count_dict.pop()
#         res = list(count_dict.keys())[0]
#         return res

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
            print(x)
        return x


if __name__ == '__main__':
    nums = [3, 4, 12, 4]
    s = Solution()
    x = s.singleNumber(nums)
    print(x)