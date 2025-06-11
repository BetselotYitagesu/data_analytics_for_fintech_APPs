""" 
This is Python code to store data into database
"""


import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Load CSV file
df = pd.read_csv("E:/Tenx/Week 2/data/processed/sentiment_reviews.csv")

# Optional: convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Database connection
conn = psycopg2.connect(
    dbname="fintech_reviews",
    user="postgres",
    password="Admin123",  # replace with your actual password
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# SQL insert query (without specifying id — auto-incremented)
query = """
INSERT INTO sentiment_review (
    review,
    rating,
    review_date,
    bank,
    source,
    sentiment_label,
    sentiment_score
) VALUES %s
"""

# Prepare the data for insertion
data = [
    (
        row['review'],
        int(row['rating']) if not pd.isnull(row['rating']) else None,
        row['date'].date() if not pd.isnull(row['date']) else None,
        row['bank'],
        row['source'],
        row['sentiment_label'],
        float(row['sentiment_score']) 
        if not pd.isnull(row['sentiment_score']) 
        else None
    )
    for _, row in df.iterrows()
]


# Execute batch insert
execute_values(cur, query, data)

# Commit and close
conn.commit()
cur.close()
conn.close()

print("✅ Data inserted successfully.")
