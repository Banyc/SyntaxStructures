using System.Collections.Generic;

namespace BlazorWebsite.Models.SyntaxVisualization
{
    public class GroupedSentence
    {
        public int GroupIndex { get; set; }
        public string Diagraph { get; set; }
        public int Count { get; set; }
    }

    public class GetGraphOfFirstTreeOfEachFreqencyGroupResponseDto : GetGraphOfFirstTreeOfEachFreqencyGroupRequestDto
    {
        public List<GroupedSentence> Groups { get; set; }
        public int NumGroups { get; set; }
    }
}
