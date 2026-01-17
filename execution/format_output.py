def format_results(posts):
    """
    Formats the list of posts into a string.
    """
    if not posts:
        return "No results found."
        
    output_lines = []
    for i, post in enumerate(posts, 1):
        output_lines.append(f"{i}. {post.get('title')}")
        output_lines.append(f"   Link: {post.get('link')}")
        # Truncate summary if too long for cleaner output
        summary = post.get('summary', '')
        if len(summary) > 200:
            summary = summary[:197] + "..."
        output_lines.append(f"   Summary: {summary}")
        output_lines.append("") # Empty line separator
        
    return "\n".join(output_lines)
