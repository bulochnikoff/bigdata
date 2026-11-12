import duckdb

con = duckdb.connect("warehouse.duckdb")
con.execute("drop table if exists reviews_clean")
con.execute(
    """
    create table reviews_clean (
        asin varchar,
        rating double,
        text varchar,
        verified_purchase boolean
    )
    """
)
con.execute(
    """
    insert into reviews_clean values
        ('B001', 5, 'good', true),
        ('B001', 3, 'ok', false),
        ('B002', 4, 'fine', true)
    """
)
print("warehouse rows", con.execute("select count(*) from reviews_clean").fetchone()[0])
