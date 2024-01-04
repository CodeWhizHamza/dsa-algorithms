from typing import List


def bubble_sort(numbers: List[int]):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


lst = [5, 2, 4, 6, 1, 3, 2, 6]
bubble_sort(lst)
print(lst)
