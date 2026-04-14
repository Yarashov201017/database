from korxona import new_connect

conn  = new_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE korxona"
# )

# cur.execute(
#     """
#     CREATE TABLE ishchilar(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(80)

#     )
#     """
# )
# print('oxshadi')
# cur.execute(
#     """
#     CREATE TABLE ish(
#         id SERIAL PRIMARY KEY,
#         work VARCHAR(101)
#     )
#     """
    
# )
# print("yes")

# cur.execute(
#     """
#     CREATE TABLE enrolments(
#         ishchi_name INTEGER,
#         ish_turi INTEGER
#     )
#     """
# )
# print("table")

# cur.execute(
#     "INSERT INTO ishchilar(name) VALUES('Yoqubboy')"
# )
# cur.execute(
#     "INSERT INTO ishchilar(name) VALUES('Valijon')"
# )
# print("ishchi qo'shildi")
# cur.execute(
#     "DELETE FROM ishchilar WHERE ID='3'"
# )
# print("ishi boshatildi")
# cur.execute(
#     "INSERT INTO ish(work) VALUES('IT ingenering')"
# )
# cur.execute(
#     "INSERT INTO ish(work) VAlUES('Dasturchi')"
# )
# print("ishcilar ishi qo'shildi")

# cur.execute(
#     "SELECT * FROM enrolments"
# )
# rows = cur.fetchall()
# print(rows)

# cur.execute(
#     "INSERT INTO enrolments(ishchi_name,ish_turi) VALUES(1,1)"
# )
# print("done")

# cur.execute(
#     "SELECT ishchilar.name ,ish.work FROM enrolments JOIN ishchilar ON ishchilar.id =enrolments.ishchi_name JOIN ish ON ish.id = enrolments.ish_turi "
# )

# rows = cur.fetchall()

# print(rows)