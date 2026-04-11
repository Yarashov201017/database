# import psycopg2

# ulash=psycopg2.connect(
#     host="localhost",
#     database="it_park",
#     user="postgres",
#     password="ulugbek"
# )
# ishlash=ulash.cursor()

# ishlash.execute(
#     "INSERT INTO student (name, age ) VALUES ('Ulugbek',15)"

# ulash.commit()


# ishlash.execute(
#     "DELETE FROM student WHERE ID='25'",
    
# )

# ishlash.execute(
#     "SELECT * FROM student"
# )

# ustunlar=ishlash.fetchall()
# for ustun in ustunlar:
#     print(ustun)

# ishlash.execute(
#     "UPDATE student SET age = 16"
# )
# ulash.commit()
import psycopg2
ulash=psycopg2.connect(
    host="localhost",
    database="new",
    user="postgres",
    password="ulugbek"
)
ulash.autocommit=True
connect=ulash.cursor()

# connect.execute(
#     "CREATE DATABASE new"
# )
# print("aa")
# connect.execute(
#     """
#     CREATE TABLE narsalar(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(101),
#         age INTEGER,
#         subject VARCHAR(101)
#     )
#     """
# )
# print("jadval tayyor")

# connect.execute(
#     """
#     CREATE TABLE ustoz(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(101),
#         age INTEGER,
#         subject VARCHAR(101)
#     )
#     """
# )
# print("jadval tayyor")
# connect.execute(
#     "INSERT INTO narsalar (name, age ,subject) VALUES ('Ulugbek',15,'Backend')"
# )
connect.execute(
    "INSERT INTO ustoz (name,age,subject) VALUES ('Mirzabek',25,'Dasturlash')"
)
ulash.commit()
