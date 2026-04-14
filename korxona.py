import psycopg2
def new_connect():
    con=psycopg2.connect(
        host="localhost",
        database="korxona",
        user="postgres",
        password="ulugbek"
    )
    return con