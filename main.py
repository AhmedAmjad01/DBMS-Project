import psycopg2
from config import config


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