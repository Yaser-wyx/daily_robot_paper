const searchRoot = document.querySelector("[data-search-index-url]");
const searchIndexUrl = searchRoot?.dataset.searchIndexUrl || "search-index.json";
const searchInput = document.getElementById("paper-search-input");
const searchCount = document.getElementById("paper-search-count");
const searchResults = document.getElementById("paper-search-results");
let paperIndex = [];

function normalizeQuery(value) {
    return (value || "").toLowerCase().trim().split(/\s+/).filter(Boolean);
}

function escapeHtml(value) {
    return String(value || "").replace(/[&<>"']/g, (char) => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        "\"": "&quot;",
        "'": "&#39;"
    }[char]));
}

function itemScore(item, terms) {
    const title = (item.title || "").toLowerCase();
    const paperId = (item.paper_id || "").toLowerCase();
    const keywords = (item.keywords || []).join(" ").toLowerCase();
    const summary = (item.summary || "").toLowerCase();
    const searchText = item.search_text || "";
    let score = 0;
    for (const term of terms) {
        if (!searchText.includes(term)) {
            return -1;
        }
        if (paperId.includes(term)) score += 60;
        if (title.includes(term)) score += 35;
        if (keywords.includes(term)) score += 18;
        if (summary.includes(term)) score += 10;
    }
    const dateValue = Date.parse(item.date || "") || 0;
    return score + dateValue / 1000000000000;
}

function renderResults() {
    const terms = normalizeQuery(searchInput.value);
    if (!terms.length) {
        searchResults.innerHTML = "";
        searchCount.textContent = `${paperIndex.length} papers indexed`;
        return;
    }

    const matches = paperIndex
        .map((item) => ({ item, score: itemScore(item, terms) }))
        .filter((entry) => entry.score >= 0)
        .sort((left, right) => right.score - left.score)
        .slice(0, 20);

    searchCount.textContent = `${matches.length} shown`;
    if (!matches.length) {
        searchResults.innerHTML = '<div class="empty-state">No matching papers found.</div>';
        return;
    }

    searchResults.innerHTML = matches.map(({ item }) => {
        const links = [
            item.html_url ? `<a class="result-link" href="${escapeHtml(item.html_url)}" target="_blank" rel="noopener noreferrer">HTML</a>` : "",
            item.pdf_url ? `<a class="result-link" href="${escapeHtml(item.pdf_url)}" target="_blank" rel="noopener noreferrer">PDF</a>` : "",
            `<a class="result-link" href="${escapeHtml(item.report_url)}">Report</a>`
        ].filter(Boolean).join("");
        const summary = item.summary ? `<p>${escapeHtml(item.summary)}</p>` : "";
        const paperId = item.paper_id ? `<span class="result-chip">${escapeHtml(item.paper_id)}</span>` : "";
        return `
            <article class="search-result">
                <div class="search-result-meta">
                    <span class="result-chip">${escapeHtml(item.date)}</span>
                    <span class="result-chip">${escapeHtml(item.section)}</span>
                    ${paperId}
                </div>
                <h3><a href="${escapeHtml(item.report_url)}">${escapeHtml(item.title)}</a></h3>
                ${summary}
                <div class="search-result-links">${links}</div>
            </article>
        `;
    }).join("");
}

fetch(searchIndexUrl)
    .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
    })
    .then((items) => {
        paperIndex = Array.isArray(items) ? items : [];
        searchCount.textContent = `${paperIndex.length} papers indexed`;
        searchInput.disabled = false;
    })
    .catch(() => {
        searchCount.textContent = "Search unavailable";
        searchInput.disabled = true;
    });

searchInput.addEventListener("input", renderResults);
