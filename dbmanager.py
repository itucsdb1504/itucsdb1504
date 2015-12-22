import psycopg2
from Venue import Venue
from News import News
from Ticket import Ticket
from Advertise import Advertise
from Award import Award
from Channel import Channel
from Comment import Comment
from Match import Match
from Player import Player
from Record import Record
from Sponsor import Sponsor
from Tournament import Tournament
from User import User
from Video import Video
from Social_accounts import Social_accounts
import utils

"""For local tests, Not used!!"""
conn_string = "host='localhost' port='5432' dbname='postgres' user='postgres' password='Abcd1234'"

"""IsTableExists and create table methods are used in begining of the project. Now, don't use."""
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

       temp_ticket = Ticket(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       ticketList.append(temp_ticket)

       row = cursor.fetchone()

    for temp_ticket in ticketList:

        cursor.execute("SELECT name FROM venues WHERE id='%s'"%(temp_ticket.getVenueID()))

        row2 = cursor.fetchone()

        temp_ticket.VenueName = row2[0]

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

       channel = Channel(row[0],row[1],row[2],row[3])

       channelList.append(channel)

       row = cursor.fetchone()

    return channelList

def addChannel(name, image_url, ext_url, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO channels VALUES('%s','%s','%s','%s')"%(utils.generateID(),name, image_url,ext_url))

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

    cursor.execute("SELECT * FROM news")

    newsList = []

    row = cursor.fetchone()
    while row:

       temp_news = News(row[0],row[1],row[2],row[3],row[4])

       newsList.append(temp_news)

       row = cursor.fetchone()

    return newsList

def getNewsWithID(id,conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news WHERE id = '%s'"%(id))

    row = cursor.fetchone()

    news = News(row[0],row[1],row[2],row[3],row[4])

    return news

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

    cursor.execute("SELECT * FROM records")

    recordList = []

    row = cursor.fetchone()
    while row:

       record = Record(row[0],row[1],row[2],row[3],row[4])

       temp_player = getPlayer(record.PlayerID, conn)
       temp_video = getVideo(record.VideoID, conn)

       record.PlayerName = temp_player.FirstName + " " + temp_player.LastName
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

    cursor.execute("SELECT * FROM sponsors")

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

    for temp_tournament in tournamentList:

        cursor.execute("SELECT name FROM venues WHERE id='%s'"%(temp_tournament.getVenueID()))

        row2 = cursor.fetchone()

        temp_tournament.VenueName = row2[0]

        cursor.execute("SELECT firstname,lastname FROM players WHERE id='%s'"%(temp_tournament.getLastWinnerID()))

        row3 = cursor.fetchone()

        temp_tournament.LastWinnerName = row3[0] + " " + row3[1]

        cursor.execute("SELECT description FROM awards WHERE id='%s'"%(temp_tournament.getAwardID()))

        row4 = cursor.fetchone()

        temp_tournament.AwardName = row4[0]

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

       match.TournamentName = getTournament(match.getTournamentID(), conn).Name
       match.VenueName = getVenue(match.getVenueID(), conn).Name

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

def createAwardTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE awards ( ID VARCHAR(100) NOT NULL,Description VARCHAR(250),LastWinnerID VARCHAR(100) REFERENCES awards (ID),PRIMARY KEY (ID))")

    conn.commit()

def getAwards(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM awards")

    awardList = []

    row = cursor.fetchone()
    while row:

       temp_award = Award(row[0],row[1],row[2])

       awardList.append(temp_award)

       row = cursor.fetchone()


    return awardList

def getAward(id, conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM awards WHERE id = '%s'"%(id))

    row = cursor.fetchone()

    award = Award(row[0],row[1],row[2])

    return award

def addAward(description, last_winner_id, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO awards VALUES('%s','%s','%s')"%(utils.generateID(),description,last_winner_id))

        conn.commit()
        return 'OK'

    except Exception as e:
        print(str(e))
        pass

def deleteAward(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM awards WHERE id = '%s'"%(id))

    conn.commit()

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

       _player = Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])

       playerList.append(_player)

       row = cursor.fetchone()

    """Getting social information of players from social_accounts table"""
    for temp_player in playerList:
        cursor.execute("SELECT * FROM social_accounts WHERE id = '%s'"%(temp_player.getID()))
        row2 = cursor.fetchone()
        #temp_player.Twitter = row2[1]
        #temp_player.Instagram = row2[2]
        #temp_player.Facebook = row2[3]

    return playerList

def getPlayer(id,conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE id = '%s'"%(id))

    row = cursor.fetchone()

    _player = Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])

    return _player

def addPlayer(firstname, lastname, age, gender, email, nationality, turned_pro, location, nickname, money_list_earnings, birthday, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO players VALUES('%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s')"%(utils.generateID(), firstname, lastname, age, gender, email, nationality, turned_pro, location, nickname, money_list_earnings, birthday))

        conn.commit()


    except Exception as e:
        print(e)
        pass

def deletePlayer(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM players WHERE id = '%s'"%(id))

    conn.commit()

def addPlayerSocial(player_id,twitter_url,instagram_url,facebook_url,conn):

    cursor = conn.cursor()

    created_id = utils.generateID()

    cursor.execute("INSERT INTO social_accounts VALUES('%s','%s','%s','%s')"%(created_id, twitter_url, instagram_url, facebook_url))

    conn.commit()

def deletePlayerSocial(id,conn):
    cursor = conn.cursor()

    cursor.execute("DELETE FROM social_accounts WHERE id = '%s'"%(id))

    conn.commit()

def createSocialAccountsTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE social_accounts (ID VARCHAR(100) REFERENCES players (ID), TwitterLink VARCHAR(20), InstagramLink VARCHAR(20), FacebookLink VARCHAR(20), PRIMARY KEY (ID))")

    conn.commit()

def getSocialAccounts(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM social_accounts")

    socialAccountsList = []

    row = cursor.fetchone()
    while row:

       social_account = Social_accounts(row[0],row[1],row[2],row[3])

       socialAccountsList.append(social_account)

       row = cursor.fetchone()


    return socialAccountsList

def addSocialAccounts(twitter_account, instagram_account, facebook_account, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO social_accounts VALUES('%s','%s','%s','%s')"%(utils.generateID(), twitter_account, instagram_account, facebook_account))

        conn.commit()



    except Exception as e:
        print(str(e))
        pass

def deleteSocialAccounts(id, conn):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM social_accounts WHERE id = '%s'"%(id))

    conn.commit()

"""END KERIM YILDIRIM """

""" ISIN KIRBAS """

def createUserTable():

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (ID VARCHAR(100) NOT NULL,Firstname VARCHAR(40),Lastname VARCHAR(40),Age int,Gender VARCHAR(10),Email VARCHAR(100),AccountType VARCHAR(10),PRIMARY KEY (ID))")

    conn.commit()

def getUsers(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users ")

    userList = []

    row = cursor.fetchone()
    while row:

       user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

       userList.append(user)

       row = cursor.fetchone()

    return userList

def checkUserLogin(username, password,conn):

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM userLogin WHERE userName = '%s' AND passWord = '%s'"%(username,password))

    result = cursor.fetchone()

    if result is None:
        return None

    cursor.execute("SELECT * FROM users WHERE id = '%s'"%(result[0]))

    row = cursor.fetchone()

    _user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

    _user.Username = result[1]

    return _user

def addUser(firstname, lastname, age, gender, email,username,password,conn):

    try:

        cursor = conn.cursor()

        created_id = utils.generateID()

        cursor.execute("INSERT INTO users VALUES('%s','%s','%s','%s','%s','%s','%s')"%(created_id, firstname, lastname, age, gender, email, 'User'))

        cursor.execute("INSERT INTO userLogin VALUES('%s','%s','%s')"%(created_id,username,password))

        conn.commit()

        return 'OK'

    except Exception as e:
        print(str(e))
        return 'SameUsername'

def deleteUser(id,conn):

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
        cursor.execute("SELECT * FROM comments WHERE newsID = '%s' "%(news_id))

    else:
        cursor.execute("SELECT * FROM comments")

    commentList = []

    row = cursor.fetchone()
    while row:

       _comment = Comment(row[0],row[1],row[3],row[4],row[5])

       commentList.append(_comment)

       row = cursor.fetchone()


    return commentList

def addComment(username, newsid ,title, content, date, conn):

    try:

        cursor = conn.cursor()

        cursor.execute("INSERT INTO comments VALUES('%s','%s','%s','%s','%s','%s')"%(utils.generateID(), username, newsid, title, content, date))

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
