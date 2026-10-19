# Infosys SP/DSE & Codeforces DP Exam Intelligence Studio

An advanced AI-powered competitive programming platform and algorithmic matching studio designed for cracking **Infosys Specialist Programmer (₹9.5 LPA)** and **Digital Specialist Engineer (₹6.5 LPA)** coding assessments through targeted mastery of high-yield **Codeforces Dynamic Programming (1400–2200)** archetypes.

---

## 🚀 Key Deliverables & Included Datasets

### 1. Codeforces DP Scored & Matched Datasets
- **[`cf_dp_scored.csv`](cf_dp_scored.csv)** (1,120 Problems): Full Codeforces DP catalog rated 1400–2200 across 12 problemset pages with:
  - CF Rating, Tags, and DP Pattern / Subtype (Knapsack, Bitmask, Interval, Tree DP, Subsequence, Digit DP)
  - Brief Question Summary & Core Intuition ("Aha!" moment)
  - Detailed Step-by-Step Solution Algorithm & Concrete Dry-Run Trace on sample inputs
  - Full C++ Solutions checked against test cases
  - **Match % to Nearest Infosys Question** (with nearest question explicitly named)
  - **Exam Prediction Index (0–100%)** calibrated for 2025–2026 drives
- **[`infosys_cf_dp_matched_master.csv`](infosys_cf_dp_matched_master.csv)** (1,158 Problems): Complete matched matrix covering all Codeforces DP problems with 18 standardized columns.

### 2. Confirmed Infosys Exam Question Banks (2021–2026)
- **[`infosys_sp_dse_questions_full.csv`](infosys_sp_dse_questions_full.csv)** & **[`infosys_sp_dse_questions_master_945.csv`](infosys_sp_dse_questions_master_945.csv)** (945 Questions): Complete archive of confirmed questions from actual online assessments, interview drives, LeetCode Discuss, GitHub HackWithInfy repositories, and memory-based candidate recollections:
  - Part 1: `Q0001` through `Q0473`
  - Part 2: `Q0474` through `Q0945` (Extracted from 45-page exam archive using neural OCR)
  - Structured fields: Title, Primary Topic, CF Rating estimate, Role (SP vs DSE), Statement, Constraints, Sample Test Cases, Solution Key Idea, and C++ Snippets.
- **[`infosys_db_clean.json`](infosys_db_clean.json)** & **[`infosys-db.js`](infosys-db.js)**: Clean JSON and runtime JS format for web and analytical consumption.

### 3. Interactive Web Application
- **Live UI**: Single-page studio with dark mode glassmorphism UI.
- **Memory Sheet View**: Intuition peek, Codeforces links, progress tracker with celebration chimes.
- **Active Recall Flashcards**: 180° flip cards for spaced repetition.
- **Deep-Dive Modals**: 3-tab problem viewer with problem summary, solution code, and discussion notes.
- **Infosys Intelligence Hub**: Filter questions by SP vs DSE suitability, minimum match %, and prediction tiers (`HOT 🔥`, `HIGH ⚡`, `MODERATE 📈`).
- **AI Voice Coach (`voice-agent.js`)**: Synthetic speech narration of problem statements, inputs/outputs, and step-by-step dry runs.
- **Instant Export**: One-click **Export CSV** and **Export JSON** buttons in the navigation bar.

---

## 🧮 Algorithmic Matching & Prediction Mathematics

For every Codeforces DP problem $P$, the matching engine evaluates all $N = 945$ Infosys questions $I \in \mathcal{D}$ using a calibrated multi-factor scoring model:

$$S(P, I) = w_{\text{topic}} \cdot J_{\text{topic}}(P, I) + w_{\text{text}} \cdot S_{\text{keyword}}(P, I) + w_{\text{diff}} \cdot f_{\text{rating}}(P, I)$$

Where:
- **Jaccard Topic Overlap** $J_{\text{topic}}(P, I)$: Measures exact and subtype paradigm similarity (e.g., Knapsack, Bitmask DP, Digit DP, Tree DP, Subsequence).
- **Domain Keyword Affinity** $S_{\text{keyword}}(P, I)$: Weights high-frequency Infosys examination anchor tokens (`xor`, `mex`, `bracket`, `stock`, `gcd`, `divisible`, `component`, `sliding window`).
- **Rating Distance Decay** $f_{\text{rating}}(P, I) = \max\left(0, 1 - \frac{|\text{Rating}_P - \text{Rating}_I|}{700}\right)$.

### Prediction Index (0–100%)
$$P_{\text{index}}(P) = \min\left(99, \left\lfloor \left(0.55 \cdot \text{Likeness}_{\text{best}} + 0.30 \cdot W_{\text{Infosys}} + 0.15 \cdot F_{\text{pattern}}\right) \times 100 \right\rfloor\right)$$

- **`HOT 🔥` (Index $\ge 82\%$)**: 47 Problems — Core DP archetypes appearing with highest recurrence in SP interviews.
- **`HIGH ⚡` (Index $68\% - 81\%$)**: 326 Problems — High-probability state-transition DP problems.
- **`MODERATE 📈` (Index $50\% - 67\%$)**: 785 Problems — Advanced DP variants.

---

## 💻 Running the Web Application Locally

To run the interactive web application locally:

```bash
# Using Python
python -m http.server 8089

# Or using Node.js
npx serve .
```

Then open `http://localhost:8089` in your web browser.

---

## 📁 Repository Structure

```
├── index.html                           # Main web app layout & modals
├── styles.css                           # Glassmorphic dark theme CSS
├── app.js                               # Application state, filters & search logic
├── matcher.js                           # Algorithmic matching & prediction engine
├── voice-agent.js                       # Web Speech API voice coach
├── data.js                              # Web dataset containing 1,158 DP problems
├── infosys-db.js                        # Web database containing 945 Infosys questions
├── cf_dp_scored.csv                     # Scored 1,120 Codeforces DP problems with C++
├── infosys_cf_dp_matched_master.csv     # Master 1,158 CF DP problems matched to Infosys
├── infosys_sp_dse_questions_full.csv    # Full 945 Infosys questions with solutions
├── infosys_sp_dse_questions_master_945.csv # Formatted master 945 Infosys questions
├── infosys_db_clean.json                # Structured JSON database of 945 Infosys questions
├── cf_dp_1158_full.json                 # Complete raw JSON dataset of 1,158 DP problems
├── extract_all_part2.py                 # Neural OCR extraction pipeline for Part 2
├── build_master_945_infosys_db.py       # Pipeline merging Part 1 & Part 2 into 945 questions
├── export_matched_csv.js                # CSV generation & matching matrix exporter
└── README.md                            # Comprehensive documentation
```
