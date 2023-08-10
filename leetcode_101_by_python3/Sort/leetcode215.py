from typing import List
import random

def findKthLargest(nums: List[int], k: int) -> int:
    def partition(arr: List[int], low: int, high: int) -> int:
        pivot = arr[low]
        left, right = low, high
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]

            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]

        arr[left] = pivot
        return left

    def randomPartition(arr: List[int], low: int, high: int) -> int:
        pivot_idx = random.randint(low, high)  # 随机选择pivot
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]  # pivot放置到最左边
        return partition(arr, low, high)  # 调用partition函数

    def topKSplit(arr: List[int], low: int, high: int, k: int) -> int:
        mid = randomPartition(arr, low, high)  # 以mid为分割点【随机选择pivot】
        if mid == k - 1:  # 第k小元素的下标为k-1
            return arr[mid]  # 【找到即返回】
        elif mid < k - 1:
            return topKSplit(arr, mid + 1, high, k)  # 递归对mid右侧元素进行排序
        else:
            return topKSplit(arr, low, mid - 1, k)  # 递归对mid左侧元素进行排序

    n = len(nums)
    return topKSplit(nums, 0, n - 1, n - k + 1)  # 第k大元素即为第n-k+1小元素


if __name__ == '__main__':
    a = [3, 2, 1, 8, 9, 5]
    k = 2

    aa = findKthLargest(a, k)
    print(aa)