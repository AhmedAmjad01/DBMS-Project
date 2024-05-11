import psycopg2
import tkinter
from tkinter import messagebox
from config import config
import firebase_admin
from firebase_admin import credentials, firestore
try:
        conn = psycopg2.connect(
        dbname="pokedex",
        user="postgres",
        password="pgadmin4",
        host="localhost",
        port="5432"
        )
        cur = conn.cursor()
        messagebox.showinfo(title="Connection Successful", message="Database postgres connected succesfully")
except psycopg2.Error as e:
       messagebox.showerror(title="Error",message=f"Error while connecting: {e}")
def connect():
    connection = None
    try:
            params = config()
            print ('connecting to postgresql')
            connection = psycopg2.connect(**params)


            crsr = connection.cursor()
            print('postgres version: ')
            crsr.execute('SELECT version()')
            db_version = crsr.fetchone()
            print(db_version)
    except(Exception, psycopg2.DatabaeError) as error:
            print (error)
    finally:
           if connection is not None:
                  connection.close()
                  print('Database connect')
if __name__ == "__main__":
       connect()