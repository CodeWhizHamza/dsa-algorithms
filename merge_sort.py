from typing import List


def merge(numbers: List[int], start: int, mid: int, end: int) -> None:
    temp: List[int] = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if numbers[i] < numbers[j]:
            temp.append(numbers[i])
            i += 1
        else:
            temp.append(numbers[j])
            j += 1

    while i <= mid:
        temp.append(numbers[i])
        i += 1

    while j <= end:
        temp.append(numbers[j])
        j += 1

    k = start
    for num in temp:
        numbers[k] = num
        k += 1


def merge_sort(numbers: List[int], start: int, end: int) -> None:
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort(numbers, start, mid)
    merge_sort(numbers, mid + 1, end)
    merge(numbers, start, mid, end)


lst = [5, 2, 4, 6, 1, 3, 2, 6]
merge_sort(lst, 0, len(lst) - 1)
print(lst)
