import psycopg2
def db_connect():
    conn=psycopg2.connect(
        host="localhost",
        database="ulugbekk",
        user="postgres",
        password="ulugbek"
    )
    return conn