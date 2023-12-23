from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for value in arr:
            if not stack or value >= stack[-1]:
                stack.append(value)
            else:
                max_ = stack.pop()
                while stack and stack[-1] > value:
                    stack.pop()
                stack.append(max_)
        return len(stack)




if __name__ == '__main__':
    arr = [0,2,1,4,3]
    # res = arr.pop(-1)
    # print(res)
    s = Solution()
    ret = s.maxChunksToSorted(arr)
    print(ret)

    pass