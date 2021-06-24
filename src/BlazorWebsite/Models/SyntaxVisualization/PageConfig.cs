namespace BlazorWebsite.Models.SyntaxVisualization
{
    
    public class PageConfig
    {
        public int PageIndex { get; set; } = 1;
        public int PageSize { get; set; } = 10;
        public (int, int) GetRange()
        {
            int fromIndex = (this.PageIndex - 1) * this.PageSize;
            int toIndex = this.PageIndex * this.PageSize;
            return (fromIndex, toIndex);
        }
    }
}
