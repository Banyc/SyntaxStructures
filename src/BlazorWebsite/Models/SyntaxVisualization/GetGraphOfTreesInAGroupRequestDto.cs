namespace BlazorWebsite.Models.SyntaxVisualization
{
    public class GetGraphOfTreesInAGroupRequestDto
    {
        public int GroupIndex { get; set; }
        public int FromOffsetIndex { get; set; }
        public int ToOffsetIndex { get; set; }
    }
}
