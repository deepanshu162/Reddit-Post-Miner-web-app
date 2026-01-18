from flask import Flask, render_template, request, jsonify
from execution import fetch_search_rss
from execution import parse_posts
from execution import rank_posts
import sys
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Configure UTF-8 for console output
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({"error": "Query cannot be empty"}), 400

    try:
        # 1. Fetch
        rss_content = fetch_search_rss.fetch_rss(query)
        if not rss_content:
            return jsonify({"error": "Failed to fetch data from Reddit"}), 502

        # 2. Parse
        posts = parse_posts.parse_xml(rss_content)
        
        # 3. Rank
        top_posts = rank_posts.rank_posts(posts, query)
        
        return jsonify({"results": top_posts})
        
    except Exception as e:
        print(f"Server Error: {e}", file=sys.stderr)
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)



