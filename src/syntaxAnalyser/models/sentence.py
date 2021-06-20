from syntaxAnalyser.models.node import *


class Sentence:
    def __init__(self) -> None:
        self.constituencyStructure: Node = None
        self.parsedString: str = None
        self.text: str = None
