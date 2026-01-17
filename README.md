<body>

<h1>🔍 Reddit Post Miner</h1>

<p>
<strong>Reddit Post Miner</strong> is a lightweight Python-based tool that fetches, filters, ranks, and formats
top relevant Reddit posts using Reddit’s <strong>RSS search feed</strong> — no API keys required.
</p>

<p>
This project is ideal for topic-based Reddit mining, trend analysis, and building news-style curated feeds.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
    <li>🔎 Accepts user search queries</li>
    <li>📡 Fetches Reddit posts via RSS (no authentication)</li>
    <li>🧹 Parses and cleans Reddit post content</li>
    <li>🧠 Ranks posts based on keyword relevance</li>
    <li>🏆 Returns the top 10 most relevant posts</li>
    <li>📝 Outputs title, summary, and direct Reddit link</li>
</ul>

<hr>

<h2>🧠 Workflow</h2>
<pre>
User Query
   ↓
Fetch Reddit RSS Feed
   ↓
Parse & Clean Posts
   ↓
Rank by Relevance
   ↓
Format Output
   ↓
Top 10 Reddit Posts
</pre>

<hr>

<h2>📂 Project Structure</h2>
<pre>
.
├── main.py
└── execution/
    ├── fetch_search_rss.py
    ├── parse_posts.py
    ├── rank_posts.py
    └── format_output.py
</pre>

<hr>

<h2>▶️ How to Run</h2>

<h3>1️⃣ Install Dependencies</h3>
<pre>pip install requests</pre>

<h3>2️⃣ Run the Program</h3>
<pre>python main.py</pre>

<h3>3️⃣ Enter a Search Query</h3>
<pre>Enter search query: machine learning</pre>

<hr>

<h2>📤 Sample Output</h2>
<pre>
1. Best Machine Learning Resources in 2025
   Link: https://www.reddit.com/r/MachineLearning/comments/...
   Summary: A curated list of ML resources including courses, books...

2. How I learned ML in 6 months
   Link: https://www.reddit.com/r/learnmachinelearning/comments/...
   Summary: My roadmap, mistakes, and advice for beginners...
</pre>

<hr>

<h2>⚙️ Why RSS Instead of Reddit API?</h2>
<ul>
    <li>No API keys required</li>
    <li>No OAuth setup</li>
    <li>No rate-limit complexity</li>
    <li>Perfect for quick prototyping and research</li>
</ul>


<hr>

<h2>📜 License</h2>
<p>
This project is open-source and free to use for learning, research, and development.
</p>

<hr>

<h2>👨‍💻 Author</h2>
<p>
Built by <strong>Deepanshu Gupta</strong><br>
If you find this project useful, consider starring the repository ⭐
</p>

</body>
