def rank_posts(posts, query):
    """
    Ranks posts based on keyword relevance and valid data.
    Returns the top 10 posts.
    """
    if not posts:
        return []
    
    query_terms = query.lower().split()
    
    scored_posts = []
    
    seen_links = set()
    
    for post in posts:
        # Deduplication
        link = post.get('link')
        if link in seen_links:
            continue
        seen_links.add(link)
        
        # Scoring
        score = 0
        title = post.get('title', '').lower()
        summary = post.get('summary', '').lower()
        
        # Basic keyword scoring
        for term in query_terms:
            if term in title:
                score += 10
            if term in summary:
                score += 2
        
        # We can also parse the date and give a small boost for recency if we needed complex logic,
        # but for now, keyword relevance is primary logic + original order (which is usually time-based from Reddit).
        
        scored_posts.append({
            "post": post,
            "score": score
        })
        
    # Sort by score descending
    scored_posts.sort(key=lambda x: x['score'], reverse=True)
    
    # Extract top 10
    top_posts = [x['post'] for x in scored_posts[:10]]
    
    return top_posts
