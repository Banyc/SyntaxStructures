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
    def post(self):
        global sortedGroupedSyntaxTrees
        json_data = request.get_json(force=True)
        filePath = json_data["filePath"]
        sortedGroupedSyntaxTrees = analyser.getSortedGroupedSubtreesFromFile(filePath)
        return {'status': 'good'}


class GetGraphOfFirstTreeOfEachFreqencyGroup(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        fromGroupIndex = json_data["fromGroupIndex"]
        toGroupIndex = json_data["toGroupIndex"]

        selected = sortedGroupedSyntaxTrees[fromGroupIndex:toGroupIndex]
        groups: List[dict] = []
        currentGroupIndex = fromGroupIndex
        for treeInfoSet in selected:
            firstTreeInfo = treeInfoSet.treeInfos[0]
            digraph = SyntaxStructureParser.getVisualizer(firstTreeInfo.root)
            groups.append({
                'groupIndex': currentGroupIndex,
                'digraph': digraph,
                'count': len(treeInfoSet.treeInfos)
            })
            currentGroupIndex += 1

        return {
            'groups': groups,
            'fromGroupIndex': fromGroupIndex,
            'toGroupIndex': toGroupIndex,
            'numGroups': len(sortedGroupedSyntaxTrees),
        }


class GetGraphOfTreesInAGroup(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        groupIndex = json_data["groupIndex"]
        fromOffsetIndex = json_data["fromOffsetIndex"]
        toOffsetIndex = json_data["toOffsetIndex"]

        selectedGroup = sortedGroupedSyntaxTrees[groupIndex]
        selectedTreeInfos = selectedGroup.treeInfos[fromOffsetIndex:toOffsetIndex]
        sentences: List[dict] = []
        currentOffsetIndex = fromOffsetIndex
        for treeInfo in selectedTreeInfos:
            digraph = SyntaxStructureParser.getVisualizer(treeInfo.root)
            sentences.append({
                'offsetIndex': currentOffsetIndex,
                'digraph': digraph,
                'fullText': treeInfo.sourceSentence.text
            })
            currentOffsetIndex += 1

        return {
            'sentences': sentences,
            'groupIndex': groupIndex,
            'fromOffsetIndex': fromOffsetIndex,
            'toOffsetIndex': toOffsetIndex,
            'numOffsets': len(selectedGroup.treeInfos),
        }


api.add_resource(HelloWorld, '/')
api.add_resource(StartGroupingSubtreesOnFile, '/StartGroupingSubtreesOnFile')
api.add_resource(GetGraphOfFirstTreeOfEachFreqencyGroup, '/GetGraphOfFirstTreeOfEachFreqencyGroup')
api.add_resource(GetGraphOfTreesInAGroup, '/GetGraphOfTreesInAGroup')

if __name__ == '__main__':
    app.run(debug=True)
