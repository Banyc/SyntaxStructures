import os
import pickle
from typing import List
from client.helpers.frequencyGraph import *
from syntaxAnalyser.syntaxAnalyser import *
from syntaxAnalyser.helpers.subtreeGrouper import *
from syntaxAnalyser.helpers.syntaxStructureParser import *
from syntaxAnalyser.models.sentenceSet import *


def main():
    analyser = SyntaxAnalyser()
    treeInfoSets = analyser.getSortedGroupedSubtreesFromFile("../tests/text/1342-0.txt")

    # draw graphs
    FrequencyGraph.draw(treeInfoSets, isLogScale=False)
    FrequencyGraph.draw(treeInfoSets, isLogScale=True)

main()
