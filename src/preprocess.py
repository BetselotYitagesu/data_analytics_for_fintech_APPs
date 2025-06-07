import pandas as pd
import os

# Load scraped data
df = pd.read_csv("../data/raw/reviews_raw.csv")

# Drop duplicates
df.drop_duplicates(subset=["review", "rating", "date"], inplace=True)

# Drop rows with missing values in important columns
df.dropna(subset=["review", "rating", "date"], inplace=True)

# Normalize date to YYYY-MM-DD
df['date'] = pd.to_datetime(df['date']).dt.date

# Reorder columns
df = df[['review', 'rating', 'date', 'bank', 'source']]

# Save cleaned file
os.makedirs("../data/processed", exist_ok=True)
df.to_csv("../data/processed/reviews_cleaned.csv", index=False)

print("✅ Preprocessing done. Cleaned data saved.")
