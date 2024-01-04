from time import perf_counter
from typing import Dict


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


def fib_with_cache(n: int) -> int:
    cache: Dict[int, int] = {}

    def fib(n: int) -> int:
        if n <= 1:
            return n

        cached = cache.get(n, None)
        if cached is not None:
            return cached

        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib(n)


for i in range(10, 991, 10):
    start = perf_counter()
    value = fib_with_cache(i)
    end = perf_counter()

    print(f"{i}: {end - start}")


graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
