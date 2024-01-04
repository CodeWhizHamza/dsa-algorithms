from typing import List


def selection_sort(numbers: List[int]):
    current = 0

    while current < len(numbers):
        min_index = current
        for j in range(min_index, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[min_index], numbers[current] = numbers[current], numbers[min_index]
        current += 1


lst = [5, 2, 4, 6, 1, 3, 2, 6]
selection_sort(lst)
print(lst)
