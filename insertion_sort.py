from typing import List


def insertion_sort(numbers: List[int]):
    for i in range(len(numbers)):
        key = numbers[i]

        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key


lst = [5, 2, 4, 6, 1, 3, 2, 6]
insertion_sort(lst)
print(lst)
