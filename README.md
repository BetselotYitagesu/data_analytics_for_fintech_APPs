# data_analytics_for_fintech_APPs

# Fintech App Review Analysis

This project focuses on analyzing customer experience from Google Play Store reviews of three major Ethiopian fintech mobile banking applications. The goal is to collect, preprocess, and prepare user-generated review data for downstream sentiment and experience analysis.

## 📱 Apps Targeted

- **Commercial Bank of Ethiopia (CBE)** – `com.combanketh.mobilebanking`
- **Bank of Abyssinia (BOA)** – `com.boa.boaMobileBanking`
- **Dashen Bank** – `com.dashen.dashensuperapp`

---

## ✅ Task 1: Data Collection & Preprocessing

### Objectives

- Scrape 400+ reviews per app using the `google-play-scraper` Python package.
- Preprocess data by cleaning, normalizing, and formatting into CSV.
- Store and manage code with a clean Git workflow (branch: `task-1`).

---

## 📁 Project Structure

fintech-app-review-analysis/
│
├── data/
│ ├── raw/ # Raw scraped reviews (CSV)
│ └── processed/ # Cleaned and normalized reviews (CSV)
│
├── src/
│ ├── scrape.py # Script to scrape reviews from Google Play Store
│ └── preprocess.py # Script to clean and preprocess the data
│
├── requirements.txt # Python dependencies
├── .gitignore # Files to ignore in Git
└── README.md # Project documentation

---

## 🧼 Preprocessing Steps

- Remove duplicate reviews
- Drop rows with missing values in `review`, `rating`, or `date`
- Normalize dates to `YYYY-MM-DD` format
- Add columns for `bank` and `source`
- Save cleaned data to: `data/processed/reviews_cleaned.csv`

---

## 📄 Output Data Schema

Each row in the cleaned dataset contains:

- `review` – Text of the user's review
- `rating` – Rating (1–5 stars)
- `date` – Date of the review in `YYYY-MM-DD` format
- `bank` – The name of the bank (CBE, BOA, or Dashen)
- `source` – Source of the review (always "Google Play")

---

## 📊 KPI Summary (Task 1)

| Metric                | Status                        |
| --------------------- | ----------------------------- |
| Total Reviews Scraped | ✅ 1,200+                     |
| Reviews per Bank      | ✅ 400+                       |
| Missing Data          | ✅ <5%                        |
| Cleaned CSV Output    | ✅ Complete                   |
| Git Commits           | ✅ Tracked on `task-1` branch |

---

## 🛠 Setup Instructions

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv fintechenv
   source fintechenv/bin/activate        # macOS/Linux
   fintechenv\Scripts\activate           # Windows

    Install dependencies:
   ```

pip install -r requirements.txt

Run the scraping script:

python src/scrape.py

Run the preprocessing script:

    python src/preprocess.py

# <<<<<<< HEAD

📌 GitHub Guidelines

    Use the task-1 branch for all Task 1 activities

    Commit frequently with clear, meaningful messages

    Use .gitignore to exclude virtual environment, cache files, etc.

🔮 Next Steps

    Sentiment analysis and topic classification

    Dashboard and data visualization

    Comparative feedback analysis across banks

## 📌 Task 2: Thematic Analysis of App Reviews

### ✅ Objective

Extract key themes and recurring topics from user reviews of three Ethiopian fintech apps (CBE, BOA, Dashen Bank) to understand common issues and suggestions.

### 🔍 What Was Done

- **Preprocessing:** Tokenized text using spaCy, removed stop words and non-alphabetic tokens, and lemmatized words.
- **Keyword/N-Gram Extraction:** Applied TF-IDF using scikit-learn to extract top keywords from each review.
- **Thematic Grouping:** Grouped keywords into themes such as Login & Access, Transaction Speed, App Stability, Customer Support, and Feature Requests.
- **Result Storage:** Saved enriched data to `data/thematic_analysis_results.csv` including review_id, review_text, sentiment_label, sentiment_score, top_keywords, and themes.

### 🛠 Tools & Libraries

Python, pandas, scikit-learn, spaCy, NLTK (for stop words), Jupyter Notebook or VS Code.

### 📁 Script Location

`scr/thematic_analysis.py`

### 📦 Output

File: `data/thematic_analysis_results.csv`  
Columns: review_id, review_text, sentiment_label, sentiment_score, top_keywords, themes

## Task 3: Store Sentiment Analysis Results in PostgreSQL

### ✅ What We Did

- Created a PostgreSQL database `fintech_reviews`
- Created a table `sentiment_reviews` with necessary columns
- Wrote and executed `scr/store_to_postgres.py` to insert cleaned sentiment data from `Sentiment_review.csv`

### 🔧 Tools Used

- PostgreSQL
- psycopg2
- pandas
- pgAdmin4

### 📁 Script Location

- `scr/store_to_postgres.py`

### 📊 Data Inserted

- CSV file: `data/Sentiment_review.csv`
- Fields inserted: review_id, review_text, sentiment_label, sentiment_score, etc.

## 📌 Task 4: Insights and Recommendations

### ✅ Objective

Derive actionable insights from sentiment scores and themes, visualize key patterns, and recommend app improvements for CBE, BOA, and Dashen Bank.

### 🔍 What Was Done

- **Insight Analysis:**  
  • Identified top drivers (positive feedback) and pain points (negative feedback) per bank by aggregating sentiment labels.  
  • Compared average sentiment scores across banks and over time.  
  • Drafted recommendations based on quantitative evidence.

- **Visualizations:**  
  • Bar chart of driver vs. pain-point review counts by bank
  • Sentiment distribution per bank
  • Line plot of average daily sentiment score by bank

- **Ethical Considerations:**  
  • Noted potential bias: more negative reviews may be posted by dissatisfied users.  
  • Highlighted sampling limits (Play Store only).

### 🛠 Tools & Libraries

Python, pandas, seaborn, matplotlib, Jupyter / VS Code, Streamlit (for future dashboard).

### 📁 Files Added

- `notebooks/visualizations/insights.ipynb`
