from flask import Flask, request
from flask_restful import Resource, Api
from syntaxAnalyser.models.treeInfo import *

from syntaxAnalyser.syntaxAnalyser import *

app = Flask(__name__)
api = Api(app)

analyser = SyntaxAnalyser()
sortedGroupedSyntaxTrees: List[TreeInfoSet] = None

sortedGroupedSyntaxTrees = analyser.getSortedGroupedSubtreesFromFile("../../tests/text/1342-0.txt")


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class StartGroupingSubtreesOnFile(Resource):
    global sortedGroupedSyntaxTrees
    def post(self):
        json_data = request.get_json(force=True)
        filePath = json_data["filePath"]
        sortedGroupedSyntaxTrees = analyser.getSortedGroupedSubtreesFromFile(filePath)
        return {'status': 'good'}


class GetGraphOfFirstTreeOfEachFreqencyGroup(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        fromGroupIndex = json_data["fromGroup"]
        toGroupIndex = json_data["toGroup"]

        selected = sortedGroupedSyntaxTrees[fromGroupIndex:toGroupIndex]
        digraphs = []
        counts = []
        for treeInfoSet in selected:
            firstTreeInfo = treeInfoSet.treeInfos[0]
            digraph = SyntaxStructureParser.getVisualizer(firstTreeInfo.root)
            digraphs.append(digraph)
            counts.append(len(treeInfoSet.treeInfos))

        return {
            'digraphs': digraphs,
            'counts': counts
        }


class GetGraphOfTreesInAGroup(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        groupIndex = json_data["groupIndex"]
        fromOffsetIndex = json_data["fromOffset"]
        toOffsetIndex = json_data["toOffset"]

        selectedGroup = sortedGroupedSyntaxTrees[groupIndex]
        selectedTreeInfos = selectedGroup.treeInfos[fromOffsetIndex:toOffsetIndex]
        digraphs = []
        for treeInfo in selectedTreeInfos:
            digraph = SyntaxStructureParser.getVisualizer(treeInfo.root)
            digraphs.append(digraph)

        return {
            'digraphs': digraphs,
        }






api.add_resource(HelloWorld, '/')
api.add_resource(StartGroupingSubtreesOnFile, '/StartGroupingSubtreesOnFile')
api.add_resource(GetGraphOfFirstTreeOfEachFreqencyGroup, '/GetGraphOfFirstTreeOfEachFreqencyGroup')
api.add_resource(GetGraphOfTreesInAGroup, '/GetGraphOfTreesInAGroup')

if __name__ == '__main__':
    app.run(debug=True)
