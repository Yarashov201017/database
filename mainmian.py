from dpd import db_connect

conn=db_connect()
cur = conn.cursor()
conn.autocommit=True

# cur.execute(
#     "CREATE DATABASE ulugbekk"
# )


# print("database yaratildi")

# cur.execute(
#     """
#     CREATE TABLE telefon(
#     id SERIAL PRIMARY KEY,
#     brand VARCHAR(80),
#     price NUMERIC(100)
#     )

#     """
# )
# print("Create table")

# cur.execute(
#     "INSERT INTO telefon(brand,price) VALUES('Samsung','10000000'),('Samsung','11000000'),('Honor','10000000'),('Honor','12000000'),('Redmi','999999')"
# )
# print('qoshildi')


cur.execute(
    # "SELECT SUM(price) FROM telefon"
    # "SELECT max(price) FROM  telefon"
    # "SELECT min(price) FROM telefon"
    # "SELECT * FROM telefon WHERE brand  IN ('Redmi')"
    # "SELECT * FROM telefon WHERE brand NOT IN ('Samsung')"
    # "SELECT * FROM telefon ORDER BY brand"
    # "SELECT * FROM telefon WHERE brand ILIKE 'S%'"
    # "SELECT * FROM telefon LIMIT 3"
    # "SELECT AVG(price) FROM telefon"
    # "SELECT COUNT(id) FROM telefon"
    # "SELECT * FROM telefon WHERE  price BETWEEN 30000 AND 100000000"
    # "SELECT * FROM telefon WHERE  brand BETWEEN 'A' AND 'p'"
    
)

rows = cur.fetchall()
for row in rows:
    print(row)