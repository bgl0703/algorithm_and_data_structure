

def quick_sort(array: list, left: int, right: int):
    if left + 1 >= right:
        return list

    l, r, pivot = left, right-1, array[left]
    while l < r:
        while l < r and array[r] >= pivot:
            r -= 1
        array[l] = array[r]

        while l < r and array[l] <= pivot:
            l += 1
        array[r] = array[l]
    array[l] = pivot
    quick_sort(array, left, l)
    quick_sort(array, l+1, right)
    return array


if __name__ == '__main__':
    list1 = [3, 5, 1, 4, 9, 2]
    ret = quick_sort(list1, 0, 6)
    print(ret)








