from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    intervals_sort = sorted(intervals, key=lambda x: x[1], reverse=False)
    start = intervals_sort[0][0]
    end = intervals_sort[0][1]
    count = 0
    for interval in intervals_sort[1:]:
        s = interval[0]
        e = interval[1]
        if s >= end:
            end = e
        else:
            count += 1
            continue
    return count


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    cnt = erase_overlap_intervals(intervals)
    print(cnt)
