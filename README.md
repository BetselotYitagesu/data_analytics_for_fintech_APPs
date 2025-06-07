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

📌 GitHub Guidelines

    Use the task-1 branch for all Task 1 activities

    Commit frequently with clear, meaningful messages

    Use .gitignore to exclude virtual environment, cache files, etc.

🔮 Next Steps

    Sentiment analysis and topic classification

    Dashboard and data visualization

    Comparative feedback analysis across banks
