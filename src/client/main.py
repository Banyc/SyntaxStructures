import os
import pickle
from typing import List
from client.helpers.subtreeAnalysis import SubtreeAnalysis
from client.helpers.syntaxStructureParser import *
from client.models.sentenceSet import *

def main():
    # sentenceSet = SyntaxStructureParser.getSentenceSet("The time for action is now. It's never too late to do something.")
    # digraph: str = SyntaxStructureParser.getVisualizer(sentenceSet.sentences[0].constituencyStructure)
    # print(digraph)

    testTextList = [
        "The time for action is now. It's never too late to do something.",
        "Hi (not really).",
    ]

    analysis = getAnalysis(testTextList)

    # sort
    allTreeInfoSet = analysis.trees.values()
    sortedTrees = sorted(allTreeInfoSet, key= lambda treeInfoSet: len(treeInfoSet.treeInfos), reverse=True)

    pass


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


main()
