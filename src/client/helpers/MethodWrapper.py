import os
import pickle
from typing import List
from client.helpers.subtreeAnalysis import *
from client.helpers.syntaxStructureParser import *
from client.models.sentenceSet import *

class MethodWrapper:
    def getAnalysis(textList: List[str]) -> SubtreeAnalysis:
        fileName = "sentenceSets.pickle"
        sentenceSets: List[SentenceSet]

        # load
        if os.path.exists(fileName):
            filePointer = open(fileName, "rb")
            sentenceSets = pickle.load(filePointer)
            filePointer.close()
            pass
        else:
            # init
            sentenceSets = []
            for text in textList:
                newSentenceSet = SyntaxStructureParser.getSentenceSet(text)
                sentenceSets.append(newSentenceSet)
            # save
            if os.path.exists(fileName):
                os.remove(fileName)
            filePointer = open(fileName, "wb")
            pickle.dump(sentenceSets, filePointer)
            filePointer.close()

        analysis = SubtreeAnalysis()
        analysis.analyzeManySentenceSet(sentenceSets)
        return analysis
    
    
    def getSortedAnalysis(textList: List[str]) -> List[TreeInfoSet]:
        analysis = MethodWrapper.getAnalysis(textList)

        # sort
        allTreeInfoSet = analysis.trees.values()
        sortedTrees = sorted(allTreeInfoSet, key= lambda treeInfoSet: len(treeInfoSet.treeInfos), reverse=True)
        return sortedTrees


    def visualizeFirstSentence(text: str):
        sentenceSet = SyntaxStructureParser.getSentenceSet(text)
        digraph: str = SyntaxStructureParser.getVisualizer(sentenceSet.sentences[0].constituencyStructure)
        print(digraph)
