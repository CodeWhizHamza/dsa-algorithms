from collections import deque
from typing import Deque, Dict


GRAPH = Dict[str, Dict[str, int]]

graph: GRAPH = {
    "1": {"2": 2, "3": 4},
    "2": {"3": 1, "4": 7},
    "3": {"5": 3},
    "4": {"6": 1},
    "5": {"4": 2, "6": 5},
    "6": {},
}


def bfs(graph: GRAPH, start: str) -> None:
    visited = set()

    queue: Deque[str] = deque()
    queue.append(start)

    while len(queue) > 0:
        current = queue.popleft()

        if current in visited:
            continue

        print(current)
        visited.add(current)

        for node in graph[current]:
            if node not in visited:
                queue.append(node)


bfs(graph, "1")
