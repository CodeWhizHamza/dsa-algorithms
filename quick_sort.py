from typing import List


def partition(numbers: List[int], p: int, r: int) -> int:
    q = p
    key = numbers[r]

    for i in range(p, r):
        if numbers[i] <= key:
            numbers[q], numbers[i] = numbers[i], numbers[q]
            q += 1

    numbers[q], numbers[r] = numbers[r], numbers[q]
    return q


def quick_sort(numbers: List[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot_index = partition(numbers, start, end)
    quick_sort(numbers, start, pivot_index - 1)
    quick_sort(numbers, pivot_index + 1, end)


lst = [5, 2, 4, 6, 1, 3, 2, 6]
quick_sort(lst, 0, len(lst) - 1)
print(lst)
