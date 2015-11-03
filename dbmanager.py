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

def createTournamentTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE tournaments (ID VARCHAR(100) NOT NULL,Name VARCHAR(100),VenueID VARCHAR(100) REFERENCES venues (ID),Round VARCHAR(20),PlayerCound int,LastWinnerID VARCHAR(100) REFERENCES players (ID),AwardID VARCHAR(100) REFERENCES awards (ID),PRIMARY KEY (ID))")

    conn.commit()

def getTournaments():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tournaments ")

    tournamentList = []

    row = cursor.fetchone()
    while row:

       tournament = Tournament(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       tournamentList.append(tournament)

       row = cursor.fetchone()

    return tournamentList

def addTournament(name, venue_name, round, player_count, last_winner_name, award_name):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("SELECT ID FROM venues WHERE name = '%s'"%(venue_name))

        venue_id = cursor.fetchone()

        cursor.execute("SELECT ID FROM players WHERE name = '%s'"%(last_winner_name))

        player_id = cursor.fetchone()

        cursor.execute("SELECT ID FROM awards WHERE name = '%s'"%(award_name))

        award_id = cursor.fetchone()

        cursor.execute("INSERT INTO tournaments VALUES('%s','%s','%s','%s','%s','%s','%s')"%(utils.generateID(), name, venue_id, round, player_count, player_id, award_id))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteTournament(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM tournaments WHERE id = '%s'"%(id))

    conn.commit()

def createMatchTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE matches (ID VARCHAR(100) NOT NULL,TournamentID VARCHAR(100) REFERENCES tournaments (ID),VenueID VARCHAR(100) REFERENCES venues (ID),Player1 VARCHAR(100) REFERENCES players (ID),Player2 VARCHAR(10) REFERENCES players (ID),IsLive VARCHAR(1),Score VARCHAR(10),PRIMARY KEY (ID))")

    conn.commit()

def getMathes():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM matches ")

    matchList = []

    row = cursor.fetchone()
    while row:

       match = Sponsor(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       matchList.append(match)

       row = cursor.fetchone()

    return matchList

def addMatch(tournament_name, venue_name, player_name1, player_name2, isLive, score):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("SELECT ID FROM venues WHERE name = '%s'"%(venue_name))

        venue_id = cursor.fetchone()

        cursor.execute("SELECT ID FROM players WHERE name = '%s'"%(player_name1))

        player_id = cursor.fetchone()

        cursor.execute("SELECT ID FROM players WHERE name = '%s'"%(player_name2))

        player_id2 = cursor.fetchone()

        cursor.execute("SELECT ID FROM tournaments WHERE name = '%s'"%(tournament_name))

        award_id = cursor.fetchone()

        cursor.execute("INSERT INTO matches VALUES('%s','%s','%s','%s','%s','%s','%s')"%(utils.generateID(), tournament_name, venue_name, player_name1, player_name2, isLive, score))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteMatch(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM matches WHERE id = '%s'"%(id))

    conn.commit()
""" END """

""" KERIM YILDIRIM """

def createPlayerTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE player ( ID VARCHAR(100) NOT NULL,FIRSTNAME VARCHAR(100), LASTNAME VARCHAR(100), AGE INT, GENDER VARCHAR(100), EMAIL VARCHAR(100), NATIONALITY VARCHAR(100), TURNED_PRO VARCHAR(100), LOCATION VARCHAR(100), NICKNAME VARCHAR(100), MLE VARCHAR(100), BIRTHDAY VARCHAR(100), PRIMARY KEY (ID))")

    conn.commit()

def getPlayer():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM player ")

    playerList = []

    row = cursor.fetchone()
    while row:

       player = player(row[0],row[1],row[2],row[3])

       playerList.append(player)

       row = cursor.fetchone()

    return playerList

def addPlayer(firstname, lastname, age, gender, email, nationality, turned_pro, location, nickname, money_list_earnings, birthday):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("INSERT INTO player VALUES('%s','%s','%d','%s',%s','%s',%s','%s',%s','%s',%s')"%(utils.generateID(), firstname, lastname, age, gender, email, nationality, turned_pro, location, nickname, money_list_earnings, birthday))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deletePlayer(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM player WHERE id = '%s'"%(id))

    conn.commit()

    """END KERIM YILDIRIM """


    """ ISIN KIRBAS """

def createUserTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (ID VARCHAR(100) NOT NULL,Firstname VARCHAR(40),Lastname VARCHAR(40),Age int,Gender VARCHAR(10),Email VARCHAR(100),AccountType VARCHAR(10),PRIMARY KEY (ID))")

    conn.commit()

def getUsers():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users ")

    userList = []

    row = cursor.fetchone()
    while row:

       user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       userList.append(user)

       row = cursor.fetchone()

    return userList

def checkUserLogin(username, password):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM userLogin WHERE username = '%s' AND password = '%s'"&(username,password))

    result = cursor.fetchone()

    if(result == null):
        return False

    return True

def addUser(firstname, lastname, age, gender, email, account_type,username,password):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("INSERT INTO users VALUES('%s','%s','%s','%s','%s','%s','%s')"%(utils.generateID(), firstname, lastname, age, gender, email, account_type))

        cursor.execute("INSERT INTO userLogin VALUES('%s','%s')"%(username,password))

        conn.commit()


    except Exception as e:
        print(str(e))
        pass

def deleteUser(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = '%s'"%(id))

    conn.commit()

def createCommentTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE comments (ID VARCHAR(100) NOT NULL, Username VARCHAR(40), NewsID VARCHAR(100) REFERENCES news (ID),Title VARCHAR(100),Content VARCHAR,Date VARCHAR(20),PRIMARY KEY (ID))")

    conn.commit()

def getComments(news_id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM comments WHERE newsID = '%s' "&(news_id))

    commentList = []

    row = cursor.fetchone()
    while row:

       comment = User(row[0],row[1],row[2],row[3],row[4])

       commentList.append(comment)

       row = cursor.fetchone()

    return commentList

def addComment(username, title, content, date):

    try:

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor()

        cursor.execute("INSERT INTO comments VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(), username, title, content, date))

        conn.commit()


    except Exception as e:
        print(str(e))
        pass

def deleteComment(id):

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM comments WHERE id = '%s'"%(id))

    conn.commit()

""" END """