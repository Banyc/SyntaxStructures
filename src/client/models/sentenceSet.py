
from typing import List

from client.models.sentence import *


class SentenceSet:
    def __init__(self) -> None:
        self.sentences: List[Sentence] = []
        self.text: str = None
