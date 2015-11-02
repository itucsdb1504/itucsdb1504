import psycopg2
import Venue

conn_string = "host='localhost' port='5432' dbname='postgres' user='postgres' password='Abcd1234'"

def isTableExists(tableSchema, tableName):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '%s' AND table_name = '%s');"%(tableSchema, tableName))

    result = cursor.fetchone()

    return result[0]

def createVenueTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE venues ( ID VARCHAR(100) NOT NULL,Name VARCHAR(100),Capacity int,Location VARCHAR(30),Description VARCHAR(250),PRIMARY KEY (ID))")

    conn.commit()

def getVenues():

    if(dbmanager.isTableExists('public','venues') == False):
        dbmanager.createVenueTable()
        print("Venues Table Created!")
    else:
        print("Venues Table Already Exist!")

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Venues ")

    result = cursor.fetchall()

    return result[0]
