
from client.models.node import *
from client.models.sentence import *


class TreeInfoSet:
    def __init__(self) -> None:
        self.treeInfos: List[TreeInfo] = []


class TreeInfo:
    def __init__(self) -> None:
        self.root: Node = None
        self.sourceSentence: Sentence = None
        self.treeId: int = 0
