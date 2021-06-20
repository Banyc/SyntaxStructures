
from typing import List


class Node:
    def __init__(self) -> None:
        self.pos: str = None
        self.terminal: str = None
        self.children: List[Node] = []
        self.parent: Node = None
