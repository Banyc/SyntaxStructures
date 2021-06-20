import os
import pickle
from typing import List
from syntaxAnalyser.syntaxAnalyser import *
from syntaxAnalyser.helpers.subtreeAnalysis import *
from syntaxAnalyser.helpers.syntaxStructureParser import *
from syntaxAnalyser.models.sentenceSet import *


def main():
    analyser = SyntaxAnalyser()
    analyser.getSortedAnalysisFromFile("../tests/text/1342-0.txt")


main()
