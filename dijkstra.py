from cmath import inf
from typing import Dict, List, Set


graph = {
    "1": {"2": 2, "3": 4},
    "2": {"3": 1, "4": 7},
    "3": {"5": 3},
    "4": {"6": 1},
    "5": {"4": 2, "6": 5},
    "6": {},
}


def min_distance(queue: List[str], distances: Dict[str, float]) -> str:
    if len(queue) == 0:
        return ""

    minimum_distance_node = queue[0]
    for node in queue:
        if distances[node] < distances[minimum_distance_node]:
            minimum_distance_node = node

    return minimum_distance_node


def dijkstra(graph: Dict, start: str) -> None:
    distances: Dict[str, float] = {}
    visited: Set[str] = set()

    for key in graph:
        distances[key] = inf

    distances[start] = 0
    queue: List[str] = list(graph.keys())

    while len(queue) > 0:
        current = min_distance(queue, distances)
        visited.add(current)

        for node, cost in graph[current].items():
            if cost + distances[current] < distances[node]:
                distances[node] = cost + distances[current]

        queue.remove(current)

    print(distances)


dijkstra(graph, "1")
