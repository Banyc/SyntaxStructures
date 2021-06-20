

from typing import Dict, List
from client.models.node import *
from client.models.treeInfo import TreeInfo


class SubtreeAnalysis:
    def __init__(self, nodes: List[Node]) -> None:
        # tuple -> treeId
        self.treeIds: Dict[tuple, int] = {}
        # treeId -> treeInfo
        self.treeInfos: Dict[int, TreeInfo] = {}

        # init
        self._analyze(nodes)


    def _analyze(self, nodes: List[Node]) -> None:
        for node in nodes:
            _ = self.getTreeId(node, isUpdateCount=True)


    # return tree ID
    def getTreeId(self, root: Node, isUpdateCount: bool) -> int:
        if root is None:
            return 0
        childTreeIds: List[int] = []
        for child in root.children:
            childTreeId = self.getTreeId(child, isUpdateCount)
            childTreeIds.append(childTreeId)
        
        treeIdsKey = (root.pos, tuple(childTreeIds))
        treeId: int = -1
        if treeIdsKey in self.treeIds.keys():
            # this tree has already exists
            treeId = self.treeIds[treeIdsKey]

            if isUpdateCount:
                self.treeInfos[treeId].count += 1
        elif isUpdateCount:
            # this tree does not exist
            treeId = len(self.treeIds) + 1
            self.treeIds[treeIdsKey] = treeId

            newTreeInfo = TreeInfo()
            newTreeInfo.count = 1
            newTreeInfo.root = root
            self.treeInfos[treeId] = newTreeInfo
        
        return treeId
