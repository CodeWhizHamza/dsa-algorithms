def tower_of_hanoi(n: int, start: str, temp: str, final: str) -> None:
    if n == 1:
        print(f"Move {n} from {start} to {final}")
        return

    tower_of_hanoi(n - 1, start, final, temp)
    print(f"Move {n} from {start} to {final}")
    tower_of_hanoi(n - 1, temp, start, final)


tower_of_hanoi(3, "A", "B", "C")
