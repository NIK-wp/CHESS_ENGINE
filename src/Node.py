from src.chess import Chess


class Node:
    def __init__(self, value: Chess) -> None:
        self.value: Chess = value
        self.children: list[Node] = []
