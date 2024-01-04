from typing import List, TypeVar

T = TypeVar("T")


def print_reverse(items: List[T]) -> None:
    stack = []
    for item in items:
        stack.append(item)

    for _ in range(len(stack)):
        print(stack.pop(), end="  ")

    print()


print_reverse([1, 2, 3, 4, 5, 6, 7, 8])
print_reverse(["a", "b", "c", "d", "e", "f", "g"])
