import mysql.connector

def connect_db(user,password,host="localhost",database=""):
    try:
        myConn = mysql.connector.connect(user=user,password=password,
            host=host,
            database=database
        )
        print("Connection is created!")
        try:
            cursor = myConn.cursor()
            print("Cursor is created!")
        except Exception as e:
            print("Error: ", e)

        return myConn, cursor
    
    except Exception as e:
        print("Error de conexión: ",e)


def cursor_db(connection):
    try:
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print("Error de conexión: ",e)


def query_db(cursor,query):
    try:
        cursor.execute(query)
        return cursor
    except Exception as e:
        print("Error: ", e)


def close_cursor(cursor):
    try:
        cursor.close()
        return True
    except Exception as e:
        print("Error: ", e)


def close_connection(connection):
    try:
        connection.close()
        return True
    except Exception as e:
        print("Error: ", e)


def connection_status(connection):
    try:
        if connection.is_connected():
            print("Connection is open!")
            return True
        else:
            print("Connection is closed!")
            return False
    except Exception as e:
        print("Error:", e)