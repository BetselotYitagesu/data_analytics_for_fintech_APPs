-- connect *into* fintech_reviews, then run this file:

create table sentiment_reviews (
   review          text,
   rating          integer,
   review_date     date,
   bank            text,
   source          text,
   sentiment_label text,
   sentiment_score float
);