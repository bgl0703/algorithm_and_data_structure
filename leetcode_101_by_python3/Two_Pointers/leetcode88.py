from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1, p2, p3 = m-1, n-1, m+n-1
    while p1 >= 0 and p2 >= 0:
        num1, num2 = nums1[p1], nums2[p2]
        if num1 > num2:
            nums1[p3] = num1
            p1 -= 1
            p3 -= 1
        else:
            nums1[p3] = num2
            p2 -= 1
            p3 -= 1
    if p2 >= 0:
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
    print(nums1)


if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)