from ddp import cl_connect

clinik=cl_connect()
cur=clinik.cursor()
clinik.autocommit=True

# cur.execute(
#     "CREATE DATABASE AT_ishniklar"
# )
# print("database yartildi")

# cur.execute(
#     """
#     CREATE TABLE ismlar(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Create table")


# cur.execute(
#     """
#     CREATE TABLE kasblar(
#     id SERIAL PRIMARY KEY,
#     kasb_name VARCHAR(100)
#     )
#     """
# )
# print("Create table")



# cur.execute(
#     """
#     CREATE TABLE qoshish(
#         ish_id INTEGER,
#         kasb_id INTEGER
#     )

#     """
# )
# print("Create table")


# cur.execute(
#     "INSERT INTO ismlar(name) VALUES('Valijon')"
# )
# cur.execute(
#     "INSERT INTO ismlar(name) VALUES('Yoqquboy')"
# )
# print("ismlar qo'shildi")
# cur.execute(
#     "INSERT INTO ismlar(name) VALUES('Alibek')"
# )
# print("ismlar qo'shildi")

# cur.execute(
#     "INSERT INTO kasblar(kasb_name) VALUES('dasturchi')"
# )


# cur.execute(
#     "INSERT INTO kasblar(kasb_name) VALUES('Web dizayner')"
# )
# print("ishlar qo'shildi")
# cur.execute(
#     "SELECT ismlar.name , kasblar.kasb_name FROM ismlar LEFT JOIN kasblar ON ismlar.id = kasblar.id"
# )

# rows=cur.fetchall()
# for row in rows:
#     print(row)