import sys
from execution.fetch_search_rss import fetch_rss
from execution.parse_posts import parse_xml
from execution.rank_posts import rank_posts
from execution.format_output import format_results


def main():
    # Force UTF-8 encoding for stdout/stderr to handle emojis on Windows terminal
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

    try:
        query = input("Enter search query: ").strip()
    except EOFError:
        return

    if not query:
        print("Error: Query cannot be empty.")
        sys.exit(1)
    
    print(f"Fetching results for: {query}...\n")
    
    # 1. Fetch
    rss_content = fetch_search_rss.fetch_rss(query)
    if not rss_content:
        print("Failed to fetch RSS data.")
        sys.exit(1)
        
    # 2. Parse
    posts = parse_posts.parse_xml(rss_content)
    if not posts:
        print("No posts found or parsing failed.")
        # Proceeding to allow "No results found" output if that's desired, 
        # but here we can just stop.
    
    # 3. Rank
    top_posts = rank_posts.rank_posts(posts, query)
    
    # 4. Format
    formatted_output = format_output.format_results(top_posts)
    
    print(formatted_output)

if __name__ == "__main__":
    main()


