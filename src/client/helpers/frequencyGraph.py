import matplotlib.pyplot as plt
from syntaxAnalyser.models.treeInfo import *

import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

class FrequencyGraph:
    def draw(treeInfoSets: List[TreeInfoSet], isLogScale: bool = False):
        x = range(len(treeInfoSets))
        y = [len(treeInfoSet.treeInfos) for treeInfoSet in treeInfoSets]
        if isLogScale:
            plt.plot(x, y)
            plt.xscale('log')
            plt.yscale('log')
            plt.ylabel('log10(treeFrequency)')
            plt.xlabel('log10(treeRank)')
        else:
            plt.plot(x, y)
            plt.xlim([0, 140])
            plt.ylim([0, 2000])
            plt.ylabel('treeFrequency')
            plt.xlabel('treeRank')
        plt.show()
