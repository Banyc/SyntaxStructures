# https://www.nltk.org/book/ch08.html

from typing import Tuple
import spacy
import benepar

from client.models.node import Node
from client.models.sentence import Sentence

class SyntaxStructureParser:

    # def _buildTree(self, root: spacy.tokens.underscore.Underscore) -> Node:
    #     node = Node()
    #     if len(root.labels) == 0:
    #         parsedString: str = root.parse_string
    #         trimmed = parsedString[1:-1]
    #         splitted = trimmed.split()
    #         node.pos = splitted[0]
    #         node.terminal = splitted[1]
    #         # return None
    #     else:
    #         node.pos = root.labels[0]

    #     for child in root.children:
    #         childNode = self._buildTree(child._)
    #         if childNode is not None:
    #             node.children.append(childNode)
    #     return node

    def buildTree(parsedString: str) -> Node:
        dummyRootNode = Node()
        currentNode = dummyRootNode
        isTerminal = False
        # rootNode: Node = None
        readPointerIndex = 0
        while readPointerIndex < len(parsedString):
            
            readChar = parsedString[readPointerIndex]

            if (readChar == '('):
                isTerminal = False
                newNode = Node()
                newNode.parent = currentNode
                currentNode.children.append(newNode)
                currentNode = newNode
                pass
            elif (readChar == ' '):
                isTerminal = True
            elif (readChar == ')'):
                currentNode = currentNode.parent
            else:
                if (isTerminal):
                    if (currentNode.terminal is None):
                        currentNode.terminal = readChar
                    else:
                        currentNode.terminal += readChar
                else:
                    if (currentNode.pos is None):
                        currentNode.pos = readChar
                    else:
                        currentNode.pos += readChar

            readPointerIndex += 1
        
        # return rootNode
        dummyRootNode.children[0].parent = None
        return dummyRootNode.children[0]


    def getSentence(text: str) -> Sentence:
        sentence: Sentence = Sentence()
        sentence.text = text

        nlp = spacy.load('en_core_web_md')
        nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))
        doc = nlp(text)
        sent = list(doc.sents)[0]

        sentence.parsedString = sent._.parse_string
        # return self._buildTree(sent._)
        sentence.constituencyStructure = SyntaxStructureParser.buildTree(sent._.parse_string)
        
        return sentence


    # return digraph fragment and nodeCount and nodeId
    def _getVisualizerRecursiveImpl(nodeCount: int, root: Node) -> Tuple[str, int, int]:
        thisNodeId = nodeCount + 1
        nodeCount += 1
        digraphFragment: str = f"n{thisNodeId} [label = \"{root.pos}\"];\n"

        if root.terminal is not None:
            terminalNodeId = nodeCount + 1
            nodeCount += 1
            terminal = SyntaxStructureParser._translateTerminal(root.terminal)
            digraphFragment += f"n{terminalNodeId} [shape = plaintext, label = \"{terminal}\"];\n"
            digraphFragment += f"n{thisNodeId} -> n{terminalNodeId};\n"

        for child in root.children:
            childDigraphFragment, childNodeCount, childNodeId = \
                SyntaxStructureParser._getVisualizerRecursiveImpl(nodeCount, child)
            nodeCount = childNodeCount
            digraphFragment += f"n{thisNodeId} -> n{childNodeId};\n"
            digraphFragment += childDigraphFragment

        return digraphFragment, nodeCount, thisNodeId


    def getVisualizer(root: Node) -> str:
        nodeCount: int = 0
        digraph: str = "digraph tree {\n"

        digraphFragment, _, _ = \
            SyntaxStructureParser._getVisualizerRecursiveImpl(nodeCount, root)
        digraph += digraphFragment
        digraph += "}\n"
        return digraph
    
    def _translateTerminal(terminal: str):
        if terminal == "-LRB-":
            return "("
        if terminal == "-RRB-":
            return ")"
        return terminal

