class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        res = ""
        if num < 0:
            num = -num
            flag = False
        else:
            flag = True
        while num != 0:
            res = str(num % 7) + res

            num = num//7
            # print(num)
        if flag:
            return res
        else:
            return '-'+res


if __name__ == '__main__':


    s = Solution()
    res = s.convertToBase7(7)
    print(res)