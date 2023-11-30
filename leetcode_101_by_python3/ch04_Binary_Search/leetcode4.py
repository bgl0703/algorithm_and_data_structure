from typing import List


def find_number_in_2d_array(matrix: List[List[int]], target: int) -> bool:
    x_len = len(matrix)
    x_left, x_right = 0, x_len - 1
    y_left, y_right = 0, len(matrix[0]) - 1

    while x_left <= x_right:
        x_mid = x_left + (x_right - x_left)//2
        if matrix[x_mid][0] <= target <= matrix[x_mid][x_len - 1]:
            break
        if matrix[x_mid][x_len - 1] < target:
            x_left = x_mid + 1
        if matrix[x_mid][x_len - 1] > target:
            x_right = x_mid - 1

    if x_right < x_left:
        return False

    while y_left <= y_right:
        y_mid = y_left + (y_right - y_left)//2
        if matrix[x_mid][y_mid] == target:
            return True
        if matrix[x_mid][y_mid] < target:
            y_left = y_mid + 1
        if matrix[x_mid][y_mid] > target:
            y_right = y_mid - 1
    return False


if __name__ == '__main__':
    nums = [[2, 4, 6, 7, 8],
            [3, 5, 7, 9, 11],
            [5, 8, 9, 13, 22]]
    target = -1
    ret = find_number_in_2d_array(nums, target)
    print(ret)
