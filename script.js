document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const resultsArea = document.getElementById('resultsArea');
    const resultsList = document.getElementById('resultsList');
    const loadingBar = document.getElementById('loadingBar');

    const search = async () => {
        const query = searchInput.value.trim();
        if (!query) return;

        // UI Updates
        resultsArea.classList.remove('hidden');
        loadingBar.classList.remove('hidden');
        resultsList.innerHTML = ''; // Clear previous
        searchBtn.disabled = true;
        searchBtn.querySelector('.btn-text').textContent = 'SCANNING...';

        try {
            const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
            const data = await response.json();

            loadingBar.classList.add('hidden');
            searchBtn.disabled = false;
            searchBtn.querySelector('.btn-text').textContent = 'INITIALIZE SCAN';

            if (data.error) {
                showError(data.error);
                return;
            }

            if (!data.results || data.results.length === 0) {
                showError("NO DATA FOUND IN SECTOR");
                return;
            }

            displayResults(data.results);

        } catch (err) {
            console.error(err);
            loadingBar.classList.add('hidden');
            searchBtn.disabled = false;
            searchBtn.querySelector('.btn-text').textContent = 'INITIALIZE SCAN';
            showError("CONNECTION LOST");
        }
    };

    const displayResults = (results) => {
        results.forEach((post, index) => {
            const card = document.createElement('div');
            card.className = 'result-card';

            // Stagger animation
            card.style.animationDelay = `${index * 100}ms`;

            card.innerHTML = `
                <div class="result-title">
                    <a href="${post.link}" target="_blank">0${index + 1} // ${escapeHtml(post.title)}</a>
                </div>
                <div class="result-summary">${escapeHtml(post.summary || 'DATA CORRUPTED OR MISSING...')}</div>
                <div class="result-meta">DATE: ${escapeHtml(post.date || 'UNKNOWN')}</div>
            `;
            resultsList.appendChild(card);
        });
    };

    const showError = (msg) => {
        resultsList.innerHTML = `<div class="result-card" style="border-left-color: red; color: red;">ERROR: ${msg}</div>`;
    };

    const escapeHtml = (text) => {
        if (!text) return '';
        return text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    searchBtn.addEventListener('click', search);
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') search();
    });
});
