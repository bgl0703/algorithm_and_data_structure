from typing import List
import math


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    pre_flower = -1
    flowerbed_len = len(flowerbed)
    count = 0
    for i in range(flowerbed_len):
        if flowerbed[i] == 1:
            if pre_flower < 0:
                count = i // 2
            else:
                count += (i - pre_flower - 2) // 2

            pre_flower = i

    if pre_flower < 0:
        count = (flowerbed_len + 1) // 2
    else:
        count += (flowerbed_len - pre_flower - 1) // 2

    return n <= count




if __name__ == '__main__':
    flowerbed = [0, 0, 1, 0, 0]
    n = 1
    ret = can_place_flowers(flowerbed, n)
    print(ret)