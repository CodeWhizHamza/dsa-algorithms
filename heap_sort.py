from typing import List


def heapify(heap: List[int], N: int) -> None:
    first_non_leaf_index = N // 2

    for i in range(first_non_leaf_index, -1, -1):
        right_child = 2 * i + 1
        left_child = 2 * i

        if N > right_child:
            if heap[i] < heap[right_child]:
                heap[i], heap[right_child] = heap[right_child], heap[i]

        if N > left_child:
            if heap[i] < heap[left_child]:
                heap[i], heap[left_child] = heap[left_child], heap[i]


def heap_sort(lst: List[int]):
    to_swap_with_index = len(lst) - 1
    for i in range(len(lst)):
        heapify(lst, len(lst) - i)
        lst[0], lst[to_swap_with_index] = lst[to_swap_with_index], lst[0]
        to_swap_with_index -= 1


lst = [5, 24, 5, 6, 2, 4, 5, 6, 65, 4]
heap_sort(lst)
print(lst)
