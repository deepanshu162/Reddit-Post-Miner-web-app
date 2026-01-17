import requests
import sys

def fetch_rss(query):
    """
    Fetches the Reddit search RSS feed for a given query.
    """
    # URL encode the query manually or let requests handle params.
    # Reddit RSS URL format: https://www.reddit.com/search.rss?q={query}
    # We must provide a User-Agent to avoid 429/403 errors.
    
    url = "https://www.reddit.com/search.rss"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    params = {
        "q": query,
        "sort": "relevance" 
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}", file=sys.stderr)
        # Return None or empty string to signal failure, or re-raise
        return None

if __name__ == "__main__":
    # Test execution
    if len(sys.argv) > 1:
        print(fetch_rss(sys.argv[1]))
    else:
        print("Usage: python fetch_search_rss.py <query>")
