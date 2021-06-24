using System.Collections.Generic;
namespace BlazorWebsite.Models.SyntaxVisualization
{
    public class GetGraphOfTreesInAGroupResponseDto : GetGraphOfTreesInAGroupRequestDto
    {
        public List<string> Digraphs { get; set; }
        public int NumOffsets { get; set; }
    }
}
