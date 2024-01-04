from typing import List


def bubble_sort(numbers: List[int]):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


def insertion_sort(numbers: List[int]):
    for i in range(len(numbers)):
        key = numbers[i]

        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key


def selection_sort(numbers: List[int]):
    current = 0

    while current < len(numbers):
        min_index = current
        for j in range(min_index, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[min_index], numbers[current] = numbers[current], numbers[min_index]
        current += 1


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
bubble_sort(lst)
print(lst)
lst = [5, 2, 4, 6, 1, 3, 2, 6]
insertion_sort(lst)
print(lst)
lst = [5, 2, 4, 6, 1, 3, 2, 6]
selection_sort(lst)
print(lst)
lst = [5, 2, 4, 6, 1, 3, 2, 6]
merge_sort(lst, 0, len(lst) - 1)
print(lst)
lst = [5, 2, 4, 6, 1, 3, 2, 6]
quick_sort(lst, 0, len(lst) - 1)
print(lst)
