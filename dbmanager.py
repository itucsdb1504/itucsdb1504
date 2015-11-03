import psycopg2
from Venue import Venue
import utils

conn_string = "host='localhost' port='5432' dbname='postgres' user='postgres' password='Abcd1234'"

def isTableExists(tableSchema, tableName):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '%s' AND table_name = '%s');"%(tableSchema, tableName))

    result = cursor.fetchone()

    return result[0]

""" ILKER YAGMUR """

def createVenueTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE venues ( ID VARCHAR(100) NOT NULL,Name VARCHAR(100),Capacity int,Location VARCHAR(30),Description VARCHAR(250),PRIMARY KEY (ID))")

    conn.commit()

def getVenues():

    '''if(isTableExists('public','venues') == False):
        createVenueTable()
        print("Venues Table Created!")
    else:
        print("Venues Table Already Exist!")'''

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM venues ")

    venueList = []

    row = cursor.fetchone()
    while row:

       temp_venue = Venue(row[0],row[1],row[2],row[3],row[4])

       venueList.append(temp_venue)

       row = cursor.fetchone()

    return venueList

def addVenue(name, capacity, location, description):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("INSERT INTO venues VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(),name, capacity,location,description))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteVenue(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM venues WHERE id = '%s'"%(id))

    conn.commit()

""" END ILKER YAGMUR """

""" UGUR BUYUKYILMAZ """

def createNewsTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE news ( ID VARCHAR(100) NOT NULL,Title VARCHAR(100),Content VARCHAR(250),ImageUrl VARCHAR,ExternalUrl VARCHAR,Date VARCHAR(20),PRIMARY KEY (ID))")

    conn.commit()

def getNews():

    #if(isTableExists('public','news') == False):
        #createNewsTable()

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news ")

    newsList = []

    row = cursor.fetchone()
    while row:

       news = News(row[0],row[1],row[2],row[3],row[4])

       newsList.append(news)

       row = cursor.fetchone()

    return newsList

def addNews(title, content, image_url, date):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("INSERT INTO news VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(), title, content, image_url, date))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteNews(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM news WHERE id = '%s'"%(id))

    conn.commit()

""" END UGUR BUYUKYILMAZ """

""" ANIL YILDIRIM """

def createSponsorTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE sponsors ( ID VARCHAR(100) NOT NULL,Name VARCHAR(100),ImageUrl VARCHAR,ExternalUrl VARCHAR,PRIMARY KEY (ID))")

    conn.commit()

def getSponsor():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sponsors ")

    sponsorList = []

    row = cursor.fetchone()
    while row:

       sponsor = Sponsor(row[0],row[1],row[2],row[3])

       sponsorList.append(sponsor)

       row = cursor.fetchone()

    return sponsorList

def addSponsor(name, image_url, ext_url):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("INSERT INTO sponsors VALUES('%s','%s','%s','%s')"%(utils.generateID(), name, image_url, ext_url))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteSponsor(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM sponsors WHERE id = '%s'"%(id))

    conn.commit()

""" END ANIL YILDIRIM """