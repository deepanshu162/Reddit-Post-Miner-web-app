import xml.etree.ElementTree as ET
import html
import re
import sys

def parse_xml(xml_content):
    """
    Parses the raw XML content and returns a list of dictionaries.
    """
    if not xml_content:
        return []

    try:
        # Parse content
        root = ET.fromstring(xml_content)
        
        posts = []
        
        # Check if Atom or RSS
        if 'http://www.w3.org/2005/Atom' in root.tag:
            # Atom
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                title = entry.find('atom:title', ns)
                link_elem = entry.find('atom:link', ns)
                content = entry.find('atom:content', ns)
                updated = entry.find('atom:updated', ns)
                
                title_text = title.text if title is not None else "No Title"
                link_href = link_elem.attrib.get('href', '') if link_elem is not None else ""
                
                # Filter: strictly keep Reddit posts (which have /comments/ in URL)
                if '/comments/' not in link_href:
                    continue
                
                # Sometimes content is raw html
                summary_text = content.text if content is not None else ""
                summary = clean_html(summary_text)

                posts.append({
                    "title": title_text,
                    "link": link_href,
                    "summary": summary,
                    "date": updated.text if updated is not None else ""
                })
        else:
            # RSS 2.0
            for item in root.findall('.//item'):
                title = item.find('title')
                link = item.find('link')
                description = item.find('description')
                pubDate = item.find('pubDate')
                
                link_text = link.text if link is not None else ""
                if '/comments/' not in link_text:
                    continue
                
                posts.append({
                    "title": title.text if title is not None else "No Title",
                    "link": link_text,
                    "summary": clean_html(description.text) if description is not None else "",
                    "date": pubDate.text if pubDate is not None else ""
                })

        return posts
        
    except Exception as e:
        # Use repr to avoid unicode errors when printing to cp1252 console
        print(f"Error parsing XML: {repr(e)}", file=sys.stderr)
        return []

def clean_html(raw_html):
    """
    Removes HTML tags and decodes entities. Also removes RSS specific artifacts.
    """
    if not raw_html:
        return ""
    
    # Remove HTML tags using regex
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    
    # Decode HTML entities
    text = html.unescape(cleantext).strip()
    
    # Remove Reddit RSS artifacts
    # Pattern 1: "submitted by /u/user to r/subreddit [link] [comments]"
    text = re.sub(r'submitted by\s+/?u/[\w-]+\s+to\s+r/[\w-]+\s*\[link\]\s*\[comments\]', '', text, flags=re.IGNORECASE)
    
    # Pattern 2: Standalone [link] [comments]
    text = text.replace('[link]', '').replace('[comments]', '')
    
    return text.strip()

