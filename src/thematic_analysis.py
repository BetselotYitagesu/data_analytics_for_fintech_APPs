"""Thematic analysis script for bank app reviews using TF-IDF and SpaCy."""

from typing import List, Set, cast
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from numpy import ndarray
import spacy
from scipy.sparse import csr_matrix

# Load review data
df = pd.read_csv("data/processed_reviews.csv")  # Update path as needed

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")


def preprocess(text: str) -> str:
    """
    Clean and tokenize input text using SpaCy:
    - Lowercase
    - Remove stop words
    - Keep alphabetic tokens
    - Lemmatize
    """
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return " ".join(tokens)


# Preprocess review texts
df["clean_text"] = df["review_text"].apply(preprocess)

# TF-IDF extraction (unigrams and bigrams)
tfidf = TfidfVectorizer(
    max_df=0.85,
    min_df=5,
    ngram_range=(1, 2)
)

# Type cast for Pylance compatibility
tfidf_matrix = cast(
    csr_matrix,
    tfidf.fit_transform(df["clean_text"])
)
feature_names: ndarray = tfidf.get_feature_names_out()


def get_top_keywords(row_idx: int, top_n: int = 5) -> List[str]:
    """
    Return top N TF-IDF keywords for a given row index.
    """
    row = tfidf_matrix[row_idx].toarray().flatten()
    top_indices: List[int] = row.argsort()[-top_n:][::-1].tolist()
    return [str(feature_names[i]) for i in top_indices]


# Apply keyword extraction to all reviews
df["top_keywords"] = [get_top_keywords(i) for i in range(len(df))]


def map_theme(keywords: List[str]) -> List[str]:
    """
    Map keywords to predefined themes.
    """
    themes: Set[str] = set()
    for word in keywords:
        if word in ["login", "access", "credentials"]:
            themes.add("Login & Access")
        elif word in ["transfer", "delay", "funds"]:
            themes.add("Transaction Speed")
        elif word in ["crash", "hang", "freeze"]:
            themes.add("App Stability")
        elif word in ["design", "interface", "layout", "user"]:
            themes.add("UI/UX")
        elif word in ["help", "support", "response"]:
            themes.add("Customer Support")
    return list(themes) if themes else ["Other"]


# Map themes for each review
df["themes"] = df["top_keywords"].apply(map_theme)

# Save result to CSV
df_to_save = df[
    [
        "review_id",
        "review_text",
        "sentiment_label",
        "sentiment_score",
        "top_keywords",
        "themes"
    ]
]
df_to_save.to_csv("data/thematic_analysis_results.csv", index=False)
