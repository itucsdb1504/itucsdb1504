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

def getVenues(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM venues")

    venueList = []

    row = cursor.fetchone()
    while row:

       temp_venue = Venue(row[0],row[1],row[2],row[3],row[4])

       venueList.append(temp_venue)

       row = cursor.fetchone()


    return venueList

def getVenue(id, conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM venues WHERE id = '%s'"%(id))

    row = cursor.fetchone()

    venue = Venue(row[0],row[1],row[2],row[3],row[4])

    return venue

def addVenue(name, capacity, location, description, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO venues VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(),name, capacity,location,description))

        conn.commit()


    except Exception as e:
        print(str(e))
        pass

def deleteVenue(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM venues WHERE id = '%s'"%(id))

    conn.commit()



def createTicketTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE tickets (ID VARCHAR(100) NOT NULL,VenueID VARCHAR(100) REFERENCES venues (ID),Title VARCHAR(100),Description VARCHAR(250),Price VARCHAR(10),Date VARCHAR(20),ExtUrl VARCHAR,PRIMARY KEY (ID))")

    conn.commit()

def getTickets(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")

    ticketList = []

    row = cursor.fetchone()
    while row:

       ticket = Venue(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       ticketList.append(ticket)

       row = cursor.fetchone()

    return ticketList

def addTicket(venue_name, title, content, price, date, ext_url,conn):
    try:

        cursor = conn.cursor()

        cursor.execute("SELECT ID FROM venues WHERE name = '%s'"%(venue_name))

        venue_id = cursor.fetchone()

        cursor.execute("INSERT INTO tickets VALUES('%s','%s','%s','%s','%s','%s','%s')"%(utils.generateID(),venue_id, title, content, price, date, ext_url))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteTicket(id,conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM tickets WHERE id = '%s'"%(id))

    conn.commit()

def createChannelTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE channels (ID VARCHAR(100) NOT NULL,Name VARCHAR(100),ImageUrl VARCHAR,ExtUrl VARCHAR,PRIMARY KEY (ID))")

    conn.commit()

def getChannels(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM channels")

    channelList = []

    row = cursor.fetchone()
    while row:

       channel = Venue(row[0],row[1],row[2],row[3])

       channelList.append(channel)

       row = cursor.fetchone()

    return channelList

def addChannel(name, image_url, ext_url, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO channels VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(),name, image_url,ext_url))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteChannel(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM channels WHERE id = '%s'"%(id))

    conn.commit()

""" END ILKER YAGMUR """

""" UGUR BUYUKYILMAZ """

def createNewsTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE news ( ID VARCHAR(100) NOT NULL,Title VARCHAR(100),Content VARCHAR(250),ImageUrl VARCHAR,ExternalUrl VARCHAR,Date VARCHAR(20),PRIMARY KEY (ID))")

    conn.commit()

def getNews(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news ")

    newsList = []

    row = cursor.fetchone()
    while row:

       news = News(row[0],row[1],row[2],row[3],row[4])

       newsList.append(news)

       row = cursor.fetchone()


    return newsList

def addNews(title, content, image_url, date, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO news VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(), title, content, image_url, date))

        conn.commit()


    except Exception as e:
        print(str(e))
        pass

def deleteNews(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM news WHERE id = '%s'"%(id))

    conn.commit()


def createVideosTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE videos (ID VARCHAR(100) NOT NULL,Title VARCHAR(100),ExtUrl VARCHAR,SourceType VARCHAR(10),PRIMARY KEY (ID))")

    conn.commit()

def getVideos(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM videos ")

    videoList = []

    row = cursor.fetchone()
    while row:

       video = Video(row[0],row[1],row[2],row[3])

       videoList.append(video)

       row = cursor.fetchone()

    return videoList

def getVideo(id,conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM videos WHERE id = '%s' "%(id))

    row = cursor.fetchone()

    video = Video(row[0],row[1],row[2],row[3])

    return video

def addVideo(title, ext_url, source_type,conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO videos VALUES('%s','%s','%s','%s')"%(utils.generateID(), title, ext_url, source_type))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteVideo(id,conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM videos WHERE id = '%s'"%(id))

    conn.commit()

def createRecordTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE records (ID VARCHAR(100) NOT NULL,Description VARCHAR(200),PlayerID VARCHAR(100) REFERENCES players (ID),VideoID VARCHAR(10) REFERENCES videos (ID),Date VARCHAR(20),PRIMARY KEY (ID))")

    conn.commit()

def getRecords(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records ")

    recordList = []

    row = cursor.fetchone()
    while row:

       record = Record(row[0],row[1],row[2],row[3],row[4])

       temp_player = getPlayer(record.PlayerID, conn)
       temp_video = getVideo(record.VideoID, conn)

       record.PlayerName = temp_player.FirstName + temp_player.LastName
       record.VideoUrl = temp_video.ExtUrl

       recordList.append(record)

       row = cursor.fetchone()

    return recordList

def addRecord(description, player_name, video_url, date,conn):

    try:

        cursor = conn.cursor()

        cursor.execute("SELECT ID FROM players WHERE name = '%s'"%(player_name))

        player_id = cursor.fetchone()

        cursor.execute("SELECT ID FROM videos WHERE name = '%s'"%(video_url))

        video_id = cursor.fetchone()

        cursor.execute("INSERT INTO records VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(), description, player_id, video_id, date))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteRecord(id,conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM records WHERE id = '%s'"%(id))

    conn.commit()

""" END UGUR BUYUKYILMAZ """

""" ANIL YILDIRIM """

def createSponsorTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE sponsors ( ID VARCHAR(100) NOT NULL,Name VARCHAR(100),ImageUrl VARCHAR,ExternalUrl VARCHAR,PRIMARY KEY (ID))")

    conn.commit()

def getSponsor(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sponsors ")

    sponsorList = []

    row = cursor.fetchone()
    while row:

       sponsor = Sponsor(row[0],row[1],row[2],row[3])

       sponsorList.append(sponsor)

       row = cursor.fetchone()

    return sponsorList

def addSponsor(name, image_url, ext_url, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO sponsors VALUES('%s','%s','%s','%s')"%(utils.generateID(), name, image_url, ext_url))

        conn.commit()

    except Exception as e:
        print(str(e))
        pass

def deleteSponsor(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM sponsors WHERE id = '%s'"%(id))

    conn.commit()

def createTournamentTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE tournaments (ID VARCHAR(100) NOT NULL,Name VARCHAR(100),VenueID VARCHAR(100) REFERENCES venues (ID),Round VARCHAR(20),PlayerCound int,LastWinnerID VARCHAR(100) REFERENCES players (ID),AwardID VARCHAR(100) REFERENCES awards (ID),PRIMARY KEY (ID))")

    conn.commit()

def getTournaments(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tournaments ")

    tournamentList = []

    row = cursor.fetchone()
    while row:

       tournament = Tournament(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       tournamentList.append(tournament)

       row = cursor.fetchone()

    return tournamentList

def getTournament(id, conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tournaments WHERE id = '%s'"%(id))

    row = cursor.fetchone()

    tournament = Tournament(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

    return tournament

def addTournament(name, venue_name, round, player_count, last_winner_name, award_name, conn):

    try:

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

def deleteTournament(id,conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM tournaments WHERE id = '%s'"%(id))

    conn.commit()

def createMatchTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE matches (ID VARCHAR(100) NOT NULL,TournamentID VARCHAR(100) REFERENCES tournaments (ID),VenueID VARCHAR(100) REFERENCES venues (ID),Player1 VARCHAR(100) REFERENCES players (ID),Player2 VARCHAR(10) REFERENCES players (ID),IsLive VARCHAR(1),Score VARCHAR(10),PRIMARY KEY (ID))")

    conn.commit()

def getMathes(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM matches ")

    matchList = []

    row = cursor.fetchone()
    while row:

       match = Match(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       match.TournamentName = getTournament(match.getTournamentID(), conn)
       match.VenueName = getVenue(match.getVenueID(), conn)
       match.Player1Name = getPlayer(match.getPlayer1(), conn)
       match.Player2Name = getPlayer(match.getPlayer2(), conn)

       matchList.append(match)

       row = cursor.fetchone()

    return matchList

def addMatch(tournament_name, venue_name, player_name1, player_name2, isLive, score, conn):

    try:

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

def deleteMatch(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM matches WHERE id = '%s'"%(id))

    conn.commit()
""" END """

""" KERIM YILDIRIM """

def createPlayersTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE players ( ID VARCHAR(100) NOT NULL,FIRSTNAME VARCHAR(100), LASTNAME VARCHAR(100), AGE INT, GENDER VARCHAR(100), EMAIL VARCHAR(100), NATIONALITY VARCHAR(100), TURNED_PRO VARCHAR(100), LOCATION VARCHAR(100), NICKNAME VARCHAR(100), MLE VARCHAR(100), BIRTHDAY VARCHAR(100), PRIMARY KEY (ID))")

    conn.commit()

def getPlayers(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players ")

    playerList = []

    row = cursor.fetchone()
    while row:

       player = player(row[0],row[1],row[2],row[3])

       playerList.append(player)

       row = cursor.fetchone()


    return playerList

def getPlayer(id,conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE id = '%s'"%(id))

    row = cursor.fetchone()

    player = player(row[0],row[1],row[2],row[3])


    return player

def addPlayer(firstname, lastname, age, gender, email, nationality, turned_pro, location, nickname, money_list_earnings, birthday, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO players VALUES('%s','%s','%d','%s',%s','%s',%s','%s',%s','%s',%s')"%(utils.generateID(), firstname, lastname, age, gender, email, nationality, turned_pro, location, nickname, money_list_earnings, birthday))

        conn.commit()


    except Exception as e:
        print(str(e))
        pass

def deletePlayer(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM players WHERE id = '%s'"%(id))

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

def getComments(news_id, conn):

    cursor = conn.cursor()

    if(news_id != "null"):
        cursor.execute("SELECT * FROM comments WHERE newsID = '%s' "&(news_id))

    else:
        cursor.execute("SELECT * FROM comments")

    commentList = []

    row = cursor.fetchone()
    while row:

       comment = User(row[0],row[1],row[2],row[3],row[4])

       commentList.append(comment)

       row = cursor.fetchone()


    return commentList

def addComment(username, title, content, date, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO comments VALUES('%s','%s','%s','%s','%s')"%(utils.generateID(), username, title, content, date))

        conn.commit()



    except Exception as e:
        print(str(e))
        pass

def deleteComment(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM comments WHERE id = '%s'"%(id))

    conn.commit()


def createAdvertiseTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE advertises (ID VARCHAR(100) NOT NULL, ImageURL VARCHAR, ExtURL VARCHAR, SIZE VARCHAR(20),PRIMARY KEY (ID))")

    conn.commit()

def getAdvertises(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM advertises")

    advertiseList = []

    row = cursor.fetchone()
    while row:

       advertise = Advertise(row[0],row[1],row[2],row[3])

       advertiseList.append(advertise)

       row = cursor.fetchone()


    return advertiseList

def addAdvertise(image_url, ext_url, size, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO advertises VALUES('%s','%s','%s','%s')"%(utils.generateID(), image_url, ext_url, size))

        conn.commit()



    except Exception as e:
        print(str(e))
        pass

def deleteAdvertise(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM advertises WHERE id = '%s'"%(id))

    conn.commit()


""" END """