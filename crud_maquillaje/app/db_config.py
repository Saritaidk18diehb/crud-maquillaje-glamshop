import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",  # o tu contraseña si le pusiste una
        database="maquillaje_db",
        port=3307  # este es el puerto correcto que usa Laragon
    )
