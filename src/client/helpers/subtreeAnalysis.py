

from typing import Dict, List
from client.models.node import *
from client.models.sentences import SentenceSet
from client.models.treeInfo import *


class SubtreeAnalysis:
    def __init__(self, sentences: SentenceSet) -> None:
        # tuple -> treeId
        self.treeIds: Dict[tuple, int] = {}
        # treeId -> treeInfos
        self.trees: Dict[int, TreeInfoSet] = {}

        # init
        self._analyze(sentences)


    def _analyze(self, sentences: SentenceSet) -> None:
        for sentence in sentences.sentences:
            _ = self.getTreeId(sentence.constituencyStructure, isUpdateCount=True, sourceSentence=sentence)


    # return tree ID
    def getTreeId(self, root: Node, isUpdateCount: bool = False, sourceSentence: Sentence = None) -> int:
        if root is None:
            return 0
        childTreeIds: List[int] = []
        for child in root.children:
            childTreeId = self.getTreeId(child, isUpdateCount, sourceSentence)
            childTreeIds.append(childTreeId)
        
        treeIdsKey = (root.pos, tuple(childTreeIds))
        treeId: int = -1
        if treeIdsKey in self.treeIds.keys():
            # this tree has already exists
            treeId = self.treeIds[treeIdsKey]

        else:
            # this tree does not exist
            treeId = len(self.treeIds) + 1
            self.treeIds[treeIdsKey] = treeId

        if isUpdateCount:
            if root.terminal is None:
                if not treeId in self.trees.keys():
                    self.trees[treeId] = TreeInfoSet()

                newTreeInfo = TreeInfo()
                newTreeInfo.root = root
                newTreeInfo.sourceSentence = sourceSentence
                newTreeInfo.treeId = treeId
                self.trees[treeId].treeInfos.append(newTreeInfo)

        return treeId
