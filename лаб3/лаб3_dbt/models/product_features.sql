select
    asin,
    count(*) as n_reviews,
    avg(rating) as avg_rating,
    avg(length(text)) as avg_text_len,
    avg(case when verified_purchase then 1.0 else 0.0 end) as verified_share
from {{ source('raw', 'reviews_clean') }}
group by asin
