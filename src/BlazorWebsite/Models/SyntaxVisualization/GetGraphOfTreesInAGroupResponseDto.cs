using System.Collections.Generic;
namespace BlazorWebsite.Models.SyntaxVisualization
{
    public class SentenceInAGroup
    {
        public int OffsetIndex { get; set; }
        public string Digraph { get; set; }
        public string FullText { get; set; }
    }

    public class GetGraphOfTreesInAGroupResponseDto : GetGraphOfTreesInAGroupRequestDto
    {
        public List<SentenceInAGroup> Sentences { get; set; }
        public int NumOffsets { get; set; }
    }
}
