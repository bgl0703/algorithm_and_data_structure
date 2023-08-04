from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    if target < 2 * numbers[0] or target > 2 * numbers[right]:
        return []
    while right >= left:
        l = numbers[left]
        r = numbers[right]
        if target == l + r:
            return [left + 1, right + 1]

        if l + r > target:
            right -= 1
        else:
            left += 1
    return []


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    ret = two_sum(numbers, target)
    print(ret)



