import random


def candy(input_list: list):
    input_len = len(input_list)
    candy_list = [1] * input_len
    for i in range(input_len - 1):
        left = input_list[i]
        right = input_list[i + 1]
        if left < right:
            candy_list[i + 1] = candy_list[i] + 1
    # print(candy_list)

    for j in range(input_len - 1, 0, -1):
        left_ = input_list[j - 1]
        right_ = input_list[j]
        if right_ < left_ and candy_list[j - 1] <= candy_list[j]:
            candy_list[j - 1] = candy_list[j] + 1
    # print(candy_list)

    return sum(candy_list)


if __name__ == '__main__':
    input_list = [20, 15, 19, 4, 19, 18, 11, 15]
    # for i in range(8):
    #     input_ = random.randint(1, 20)
    #     input_list.append(input_)
    print(input_list)
    ret = candy(input_list)
    print(ret)