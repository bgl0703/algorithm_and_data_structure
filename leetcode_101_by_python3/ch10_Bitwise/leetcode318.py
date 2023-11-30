from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dict_num = self.build_number_hash_table()
        number_sum_list = []
        words_sort = sorted(words, key=lambda x: len(x), reverse=True)
        for word in words_sort:
            word = "".join(set(word))
            number_sum = 0
            for w in word:
                number_sum += dict_num.get(w)
            number_sum_list.append(number_sum)
        max_length = 0
        for i in range(len(number_sum_list)):
            for j in range(i+1, len(number_sum_list)):
                # print(f"number_sum_list[i] == {number_sum_list[i]}")
                # print(f"number_sum_list[j] == {number_sum_list[j]}")
                if number_sum_list[i] & number_sum_list[j] == 0:
                    # print(words_sort[i])
                    # print(f"--------------------")
                    # print(words_sort[j])
                    max_length = max(max_length, len(words_sort[i]) * len(words_sort[j]))
        return max_length

    def build_number_hash_table(self):
        dict_num = {}
        letter = "abcdefghijklmnopqrstuvwxyz"
        for i, l in enumerate(letter):
            dict_num[l] = 2**i
        return dict_num


if __name__ == '__main__':
    words = ["a", "aa", "aaa", "aaaa"]
    s = Solution()
    res = s.maxProduct(words)
    print(res)