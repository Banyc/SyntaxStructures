import os
import pickle
from typing import List
from client.helpers.subtreeAnalysis import *
from client.helpers.syntaxStructureParser import *
from client.models.sentenceSet import *

class MethodWrapper:
    def getAnalysis(textList: List[str], tempFilePath: str) -> SubtreeAnalysis:
        sentenceSets: List[SentenceSet]
        parser = SyntaxStructureParser()

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
                newSentenceSet = parser.getSentenceSet(text)
                sentenceSets.append(newSentenceSet)
            # save
            if os.path.exists(tempFilePath):
                os.remove(tempFilePath)
            filePointer = open(tempFilePath, "wb")
            pickle.dump(sentenceSets, filePointer)
            filePointer.close()

        analysis = SubtreeAnalysis()
        analysis.analyzeManySentenceSet(sentenceSets)
        return analysis
    
    
    def getSortedAnalysis(textList: List[str], tempFilePath: str) -> List[TreeInfoSet]:
        analysis = MethodWrapper.getAnalysis(textList, tempFilePath)

        # sort
        allTreeInfoSet = analysis.trees.values()
        sortedTrees = sorted(allTreeInfoSet, key= lambda treeInfoSet: len(treeInfoSet.treeInfos), reverse=True)
        return sortedTrees


    def visualizeFirstSentence(text: str):
        parser = SyntaxStructureParser()
        sentenceSet = parser.getSentenceSet(text)
        digraph: str = SyntaxStructureParser.getVisualizer(sentenceSet.sentences[0].constituencyStructure)
        print(digraph)


    def getSortedAnalysisFromFile(fileName: str) -> List[TreeInfoSet]:
        filePointer = open(fileName, "r", encoding="utf-8")
        text = filePointer.read()
        filePointer.close()
        textList = text.split("\n\n")
        return MethodWrapper.getSortedAnalysis(textList, tempFilePath = fileName + ".pickle")
