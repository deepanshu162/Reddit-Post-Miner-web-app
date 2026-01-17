<body>

<h1>🚀 Reddit Post Miner</h1>

<p>
Reddit Post Miner is a web-based application that allows users to search Reddit topics and instantly retrieve the <strong>top 10 most relevant posts</strong> using Reddit’s RSS feeds. The system fetches, parses, ranks, and displays results in a clean, cyber-themed interface.
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>🔍 Search Reddit posts by keyword</li>
  <li>📡 Uses Reddit <strong>RSS feeds</strong> (no API keys required)</li>
  <li>🧠 Keyword-based relevance ranking</li>
  <li>🧹 Cleans and summarizes post content</li>
  <li>🎨 Cyberpunk-style responsive UI</li>
  <li>⚡ Fast and lightweight Flask backend</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>

<h3>Backend</h3>
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>Requests</li>
  <li>XML Parsing (ElementTree)</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li>HTML5</li>
  <li>CSS3 (Cyberpunk UI)</li>
  <li>JavaScript (Fetch API)</li>
</ul>

<hr>

<h2>🏗️ Project Architecture</h2>

<pre>
Reddit-Post-Miner/
│
├── app.py                     # Flask application entry point
│
├── execution/
│   ├── fetch_search_rss.py    # Fetches Reddit RSS feeds
│   ├── parse_posts.py         # Parses and cleans RSS XML
│   ├── rank_posts.py          # Ranks posts by relevance
│   └── format_output.py       # (Optional) CLI formatter
│
├── templates/
│   └── index.html             # Frontend HTML
│
├── static/
│   ├── css/style.css          # UI styling
│   └── js/script.js           # Frontend logic
│
└── README.md
</pre>

<hr>

<h2>⚙️ How It Works</h2>
<ol>
  <li>User enters a search query</li>
  <li>App fetches Reddit search RSS feed</li>
  <li>RSS XML is parsed and cleaned</li>
  <li>Posts are ranked using keyword relevance</li>
  <li>Top 10 results are returned as JSON</li>
  <li>Frontend displays results dynamically</li>
</ol>

<hr>

<h2>▶️ How to Run Locally</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/your-username/reddit-post-miner.git
cd reddit-post-miner
</pre>

<h3>2️⃣ Install Dependencies</h3>
<pre>
pip install flask requests
</pre>

<h3>3️⃣ Run the Application</h3>
<pre>
python app.py
</pre>

<h3>4️⃣ Open in Browser</h3>
<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2>📌 Example Output</h2>
<p>Each search returns:</p>
<ul>
  <li>Post Title</li>
  <li>Cleaned Summary</li>
  <li>Direct Reddit Link</li>
  <li>Post Date</li>
</ul>

<hr>

<h2>🚧 Limitations</h2>
<ul>
  <li>Uses RSS feeds (rate-limited by Reddit)</li>
  <li>No authentication-based features</li>
  <li>Ranking is keyword-based (no ML)</li>
</ul>

<hr>

<h2>📜 License</h2>
<p>
This project is open-source and available under the <strong>MIT License</strong>.
</p>

<hr>

<h2>🙌 Acknowledgements</h2>
<ul>
  <li>Reddit RSS feeds</li>
  <li>Flask community</li>
</ul>

<p><strong>Happy Mining! 🧠🔥</strong></p>

</body>
