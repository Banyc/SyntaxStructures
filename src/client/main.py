import os
import pickle
from typing import List
from client.helpers.subtreeAnalysis import SubtreeAnalysis
from client.helpers.syntaxStructureParser import *
from client.models.sentences import *

def main():
    # sentence = SyntaxStructureParser.getSentence("The time for action is now. It's never too late to do something.")
    # digraph: str = SyntaxStructureParser.getVisualizer(sentence.constituencyStructure)
    # print(digraph)

    testTextList = [
        "The time for action is now. It's never too late to do something.",
        "Hi (not really).",
    ]

    analysis = getAnalysis(testTextList)


    pass


def getAnalysis(textList: List[str]) -> SubtreeAnalysis:
    fileName = "sentences.pickle"
    sentences: Sentences

    # load
    if os.path.exists(fileName):
        filePointer = open(fileName, "rb")
        sentences = pickle.load(filePointer)
        filePointer.close()
        pass
    else:
        # init
        sentences = Sentences()
        for text in textList:
            sentence = SyntaxStructureParser.getSentence(text)
            sentences.sentences.append(sentence)
        # save 
        if os.path.exists(fileName):
            os.remove(fileName)
        filePointer = open(fileName, "wb")
        pickle.dump(sentences, filePointer)
        filePointer.close()

    nodes = [sentence.constituencyStructure for sentence in sentences.sentences]
    analysis = SubtreeAnalysis(nodes)
    return analysis


main()