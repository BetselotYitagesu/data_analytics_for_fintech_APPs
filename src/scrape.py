import os

from google_play_scraper import reviews, Sort
import pandas as pd


def scrape_reviews(app_id, bank_name):
    result, _ = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )
    if result:
        print("Keys in first review item:", result[0].keys())
    else:
        print("No reviews fetched")

    df = pd.DataFrame(result)
    df = df[['content', 'score', 'at']]
    df.columns = ['review', 'rating', 'date']
    df['bank'] = bank_name
    df['source'] = 'Google Play'
    return df


def main():
    cbe_df = scrape_reviews("com.combanketh.mobilebanking", "CBE")
    boa_df = scrape_reviews("com.boa.boaMobileBanking", "BOA")
    dashen_df = scrape_reviews("com.dashen.dashensuperapp", "Dashen")

    all_reviews = pd.concat([cbe_df, boa_df, dashen_df])
    os.makedirs("../data/raw", exist_ok=True)
    all_reviews.to_csv("../data/raw/reviews_raw.csv", index=False)


if __name__ == "__main__":
    main()
