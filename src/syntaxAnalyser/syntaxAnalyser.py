import os
import pickle
from typing import List
from syntaxAnalyser.helpers.subtreeGrouper import *
from syntaxAnalyser.helpers.syntaxStructureParser import *
from syntaxAnalyser.models.sentenceSet import *


class SyntaxAnalyser:
    def __init__(self) -> None:
        self.parser = SyntaxStructureParser()
    
    def getSubtreeGrouper(self, textList: List[str], tempFilePath: str) -> SubtreeGrouper:
        sentenceSets: List[SentenceSet]

        # load
        if os.path.exists(tempFilePath):
            filePointer = open(tempFilePath, "rb")
            sentenceSets = pickle.load(filePointer)
            filePointer.close()
            pass
        else:
            # init
            sentenceSets = []
            for text in textList:
                newSentenceSet = self.parser.getSentenceSet(text)
                sentenceSets.append(newSentenceSet)
            # save
            if os.path.exists(tempFilePath):
                os.remove(tempFilePath)
            filePointer = open(tempFilePath, "wb")
            pickle.dump(sentenceSets, filePointer)
            filePointer.close()

        grouper = SubtreeGrouper()
        grouper.analyzeManySentenceSet(sentenceSets)
        return grouper
    
    
    def getSortedGroupedSubtrees(self, textList: List[str], tempFilePath: str) -> List[TreeInfoSet]:
        analysis = self.getSubtreeGrouper(textList, tempFilePath)

        # sort
        allTreeInfoSet = analysis.trees.values()
        sortedTrees = sorted(allTreeInfoSet, key= lambda treeInfoSet: len(treeInfoSet.treeInfos), reverse=True)
        return sortedTrees


    def visualizeFirstSentence(self, text: str):
        sentenceSet = self.parser.getSentenceSet(text)
        digraph: str = SyntaxStructureParser.getVisualizer(sentenceSet.sentences[0].constituencyStructure)
        print(digraph)


    def getSortedGroupedSubtreesFromFile(self, fileName: str) -> List[TreeInfoSet]:
        filePointer = open(fileName, "r", encoding="utf-8")
        text = filePointer.read()
        filePointer.close()
        textList = text.split("\n\n")
        return self.getSortedGroupedSubtrees(textList, tempFilePath = fileName + ".pickle")
