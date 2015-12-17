import datetime
import psycopg2 as dbapi2
import json
import os
import re
import logging

import dbmanager
from layoutInfo import layoutInfo

from flask import Flask
from flask import render_template
from flask import redirect
from flask.helpers import url_for
from flask import request
from flask import session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'itucsdb1504'

def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn



@app.route('/')
def home():

    return redirect('/news')

@app.route('/news')
def news():
    with dbapi2.connect(app.config['dsn']) as connection:
        _newsList = dbmanager.getNews(connection)
        _sponsorList = dbmanager.getSponsor(connection)
        _channelList = dbmanager.getChannels(connection)
        _info = layoutInfo('All about Snooker','Daily News for Snooker','static/img/home-bg.jpg')
        return render_template('fnews.html', newsList = _newsList, info = _info, sponsorList = _sponsorList, channelList = _channelList)

@app.route('/news/<newsid>')
def newsDetail(newsid):
    with dbapi2.connect(app.config['dsn']) as connection:
        _news = dbmanager.getNewsWithID(newsid,connection)
        _sponsorList = dbmanager.getSponsor(connection)
        _channelList = dbmanager.getChannels(connection)
        _info = layoutInfo(_news.getTitle(),'',_news.getImageUrl())
        _comments = dbmanager.getComments(newsid,connection)
        return render_template('/fnews_detail.html',news = _news, info = _info, commentList = _comments, sponsorList = _sponsorList, channelList = _channelList)

@app.route('/news/addcomment', methods=['GET','POST'])
def addCommentToNews():
    with dbapi2.connect(app.config['dsn']) as connection:
        news_id = ""
        if(request.form["action"] == "Add Comment"):
            _newsid = request.form['newsid']
            user_id = session.get('loggedUser')
            dbmanager.addComment(user_id,_newsid,request.form['comment_title'], request.form['comment_content'],datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), connection)

        return redirect(url_for('newsDetail', newsid = _newsid))

@app.route('/tickets')
def ftickets():
    with dbapi2.connect(app.config['dsn']) as connection:
        _ticketList = dbmanager.getTickets(connection)
        _sponsorList = dbmanager.getSponsor(connection)
        _channelList = dbmanager.getChannels(connection)
        _info = layoutInfo('If you go step by step, with confidence, you can go far.','RONNIE O-SULLIVAN','static/img/players.jpg')
        return render_template('ftickets.html', ticketList = _ticketList, info = _info, sponsorList = _sponsorList, channelList = _channelList)

@app.route('/matches')
def fmatches():
    with dbapi2.connect(app.config['dsn']) as connection:
        _matchList = dbmanager.getMathes(connection)
        _sponsorList = dbmanager.getSponsor(connection)
        _channelList = dbmanager.getChannels(connection)
        _info = layoutInfo('Looking for perfection is the only way.','RONNIE O-SULLIVAN','static/img/players.jpg')
        return render_template('fmatches.html', matchList = _matchList, info = _info, sponsorList = _sponsorList, channelList = _channelList)

@app.route('/records')
def frecords():
    with dbapi2.connect(app.config['dsn']) as connection:
        _recordList = dbmanager.getRecords(connection)
        _sponsorList = dbmanager.getSponsor(connection)
        _channelList = dbmanager.getChannels(connection)
        _info = layoutInfo('Never mind what others do; do better than yourself.','RONNIE O-SULLIVAN','static/img/players.jpg')
        return render_template('frecords.html', recordList = _recordList, info = _info, sponsorList = _sponsorList, channelList = _channelList)


@app.route('/tournaments')
def ftournaments():
    with dbapi2.connect(app.config['dsn']) as connection:
        _tourList = dbmanager.getTournaments(connection)
        _sponsorList = dbmanager.getSponsor(connection)
        _channelList = dbmanager.getChannels(connection)
        _info = layoutInfo('Snooker is about having the best offensive play possible.','RONNIE O-SULLIVAN','static/img/players.jpg')
        return render_template('ftournament.html', tournamentList = _tourList, info = _info, sponsorList = _sponsorList, channelList = _channelList)

@app.route('/players')
def fplayers():
    with dbapi2.connect(app.config['dsn']) as connection:
        _playerList = dbmanager.getPlayers(connection)
        _sponsorList = dbmanager.getSponsor(connection)
        _channelList = dbmanager.getChannels(connection)
        _info = layoutInfo('The game of snooker has been everything to me.','RONNIE O-SULLIVAN','static/img/players.jpg')
        return render_template('fplayers.html', playerList = _playerList, info = _info, sponsorList = _sponsorList, channelList = _channelList)

@app.route('/login', methods=['GET','POST'])
def login():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _info = layoutInfo('All about Snooker','Daily News for Snooker','static/img/home-bg.jpg')
            _advertiseList = dbmanager.getAdvertises(connection)
            if(session.get('loginStatus') == 'WrongPass'):
                _info = layoutInfo('All about Snooker','But you Enter Wrong Username or Password!!','static/img/home-bg.jpg')
            if(session.get('loginStatus') == 'SameUsername'):
                _info = layoutInfo('All about Snooker','But Username is used by Another User!!','static/img/home-bg.jpg')

            return render_template('login.html', info = _info,advertiseList=_advertiseList)
        
        if(request.form["action"] == "Log In"):
            user = dbmanager.checkUserLogin(request.form['username'], request.form['password'], connection)
            if user is not None:
                session['loggedUser'] = user.Username
                session['loggedUserID'] = user.getID()
                session['loginStatus'] = 'OK'
                if(user.getAccountType() == 'King'):
                    session['loginStatus'] = 'King'
                    return redirect(url_for('adminPage'))
                else:
                    session['loginStatus'] = 'Normal'
                    return redirect(url_for('home'))
            else:
                session['loggedUser'] = ' '
                session['loggedUserID'] = ' '
                session['loginStatus'] = 'WrongPass'
                return redirect(url_for('login'))

        if(request.form["action"] == "Register"):
            result = dbmanager.addUser(request.form['firstname'],request.form['lastname'], request.form['age'],request.form['gender'],request.form['email'],request.form['username'],request.form['password'],connection)
            session['loggedUser'] = ' '
            session['loggedUserID'] = ' '
            session['loginStatus'] = result
            if(result != 'OK'):
                return redirect(url_for('login'))
            return redirect(url_for('home'))

@app.route('/loginOut', methods=['GET','POST'])
def loginOut():
    session['loggedUser'] = ' '
    session['loggedUserID'] = ' '
    session['loginStatus'] = 'OK'
    return redirect(url_for('home'))

@app.route('/admin_panel')
def adminPage():
    if(session['loggedUser'] == ' ' or session['loginStatus'] != 'King'):
        return redirect('/')

    return render_template('admin_panel.html')

@app.route('/admin_panel/test')
def testHtml():
    return render_template('test.html')

@app.route('/admin_panel/player', methods=['GET','POST'])
def player():
    with dbapi2.connect(app.config['dsn']) as connection:

        if(request.method == 'GET'):
            _playerList = dbmanager.getPlayers(connection)
            return render_template('player.html', playerList = _playerList)

        if(request.form["action"] == "add_player_action"):
            dbmanager.addPlayer(request.form['add_firstname'], request.form['add_lastname'], request.form['add_age'], request.form['add_gender'],request.form['add_email'],request.form['add_nationality'],request.form['add_turned_pro'],request.form['add_location'],request.form['add_nickname'],request.form['add_money_list_earnings'],request.form['add_birthday'], connection)
            return redirect(url_for('player'))

        if(request.form["action"] == "delete_player_action"):
            dbmanager.deletePlayer(request.form['id'], connection)
            return redirect(url_for('player'))

@app.route('/admin_panel/news', methods=['GET','POST'])
def addNews():
    with dbapi2.connect(app.config['dsn']) as connection:

        if(request.method == 'GET'):
            _newsList = dbmanager.getNews(connection)
            return render_template('news.html', newsList = _newsList)

        if(request.form["action"] == "add_news_action"):
            dbmanager.addNews(request.form['news_title'], request.form['message'], request.form['news_imageurl'], request.form['news_date'], connection)
            return redirect(url_for('addNews'))

        if(request.form["action"] == "delete_news_action"):
            dbmanager.deleteNews(request.form['id'], connection)
            return redirect(url_for('addNews'))


@app.route('/admin_panel/record', methods=['GET','POST'])
def addRecord():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _recordList = dbmanager.getRecords(connection)
            return render_template('record.html', recordList = _recordList)

        if(request.form["action"] == "add_record_action"):
            dbmanager.addRecord(request.form['record_desc'], request.form['player_name'], request.form['video_url'],request.form['record_date'] ,connection)
            return redirect(url_for('addRecord'))

        if(request.form["action"] == "delete_record_action"):
            dbmanager.deleteRecord(request.form['id'], connection)
            return redirect(url_for('addRecord'))

        return render_template('record.html')

@app.route('/admin_panel/video', methods=['GET','POST'])
def addVideo():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _videoList = dbmanager.getVideos(connection)
            return render_template('video.html', videoList = _videoList)

        if(request.form["action"] == "add_video_action"):
            dbmanager.addVideo(request.form['add_video_title'], request.form['add_ext_url'], request.form['add_source_type'],connection)
            return redirect(url_for('addVideo'))

        if(request.form["action"] == "delete_video_action"):
            dbmanager.deleteVideo(request.form['id'], connection)
            return redirect(url_for('addVideo'))

        return render_template('video.html')

@app.route('/admin_panel/match', methods=['GET','POST'])
def addMatch():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _matchList = dbmanager.getMathes(connection)
            return render_template('match.html', matchList = _matchList)

        if(request.form["action"] == "Add Match"):
            dbmanager.addMatch(request.form['add_tournamentName'], request.form['add_venueName'], request.form['add_player1'],request.form['add_player2'], request.form['add_isLive'], request.form['add_score'],connection)
            return redirect(url_for('addMatch'))

        if(request.form["action"] == "Delete"):
            dbmanager.deleteVideo(request.form['id'], connection)
            return redirect(url_for('addMatch'))

        return render_template('match.html')


@app.route('/admin_panel/sponsor', methods=['GET','POST'])
def sponsor():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _sponsorList = dbmanager.getSponsor(connection)
            return render_template('sponsor.html', sponsorList = _sponsorList)

        if(request.form["action"] == "add_sponsor_action"):
            dbmanager.addSponsor(request.form['add_name'], request.form['add_imageURL'], request.form['add_extURL'], connection)
            return redirect(url_for('sponsor'))

        if(request.form["action"] == "delete_sponsor_action"):
            dbmanager.deleteSponsor(request.form['id'], connection)
            return redirect(url_for('sponsor'))

        return render_template('sponsor.html')

@app.route('/admin_panel/tournament', methods=['GET','POST'])
def tournament():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _tournamentList = dbmanager.getTournaments(connection)
            return render_template('tournament.html', tournamentList = _tournamentList)

        if(request.form["action"] == "add_sponsor_action"):
            dbmanager.addTournament(request.form['add_name'], request.form['add_venueName'], request.form['add_round'],request.form['add_player_count'], request.form['add_lastWinnerName'], request.form['add_awardName'], connection)
            return redirect(url_for('tournament'))

        if(request.form["action"] == "delete_sponsor_action"):
            dbmanager.deleteTournament(request.form['id'], connection)
            return redirect(url_for('tournament'))

        return render_template('tournament.html')


@app.route('/admin_panel/advertise', methods=['GET','POST'])
def advertise():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _advertiseList = dbmanager.getAdvertises(connection)
            return render_template('advertise.html', advertiseList = _advertiseList)

        if(request.form["action"] == "Add Advertise"):
            dbmanager.addAdvertise(request.form['advertise_imageurl'], request.form['advertise_exturl'], request.form['advertise_size'], connection)
            return redirect(url_for('advertise'))

        if(request.form["action"] == "Delete"):
            dbmanager.deleteAdvertise(request.form['id'], connection)
            return redirect(url_for('advertise'))

        return render_template('advertise.html')

@app.route('/admin_panel/comment', methods=['GET','POST'])
def comment():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _commentList = dbmanager.getComments("null",connection)
            return render_template('comment.html', commentList = _commentList)

        if(request.form["action"] == "Add Comment"):
            dbmanager.addComment(request.form['comment_username'], request.form['comment_title'], request.form['comment_content'], request.form['comment_date'])
            return redirect(url_for('comment'))

        if(request.form["action"] == "Delete"):
            dbmanager.deleteComment(request.form['id'])
            return redirect(url_for('comment'))

@app.route('/admin_panel/user', methods=['GET','POST'])
def user():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _userList = dbmanager.getUsers(connection)
            return render_template('user.html', userList = _userList)

        if(request.form["action"] == "Add User"):
            return redirect(url_for('user'))

        if(request.form["action"] == "Delete"):
            return redirect(url_for('user'))

@app.route('/admin_panel/venue', methods=['GET','POST'])
def venue():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _venueList = dbmanager.getVenues(connection)
            return render_template('venue.html', venueList = _venueList)

        if(request.form["action"] == "add_venue_action"):
            dbmanager.addVenue(request.form['add_name'], request.form['add_capacity'], request.form['add_location'], request.form['add_desc'], connection)
            return redirect(url_for('venue'))

        if(request.form["action"] == "delete_venue_action"):
            dbmanager.deleteVenue(request.form['id'], connection)
            return redirect(url_for('venue'))

@app.route('/admin_panel/ticket', methods=['GET','POST'])
def ticket():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _ticketList = dbmanager.getTickets(connection)
            return render_template('ticket.html', ticketList = _ticketList)

        if(request.form["action"] == "add_ticket_action"):
            dbmanager.addTicket(request.form['add_ticket_venue'], request.form['add_ticket_title'], request.form['add_ticket_content'],request.form['add_ticket_price'], request.form['add_ticket_exturl'], request.form['add_ticket_date'],connection)
            return redirect(url_for('ticket'))

        if(request.form["action"] == "delete_ticket_action"):
            dbmanager.deleteTicket(request.form['id'], connection)
            return redirect(url_for('ticket'))

@app.route('/admin_panel/channel', methods=['GET','POST'])
def channel():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _channelList = dbmanager.getChannels(connection)
            return render_template('channel.html', channelList = _channelList)

        if(request.form["action"] == "Add Channel"):
            dbmanager.addChannel(request.form['add_channel_name'], request.form['add_channel_imageurl'], request.form['add_channel_exturl'], connection)
            return redirect(url_for('channel'))

        if(request.form["action"] == "Delete"):
            dbmanager.deleteChannel(request.form['id'], connection)
            return redirect(url_for('channel'))

        return render_template('channel.html')

@app.route('/admin_panel/award', methods=['GET','POST'])
def award():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _awardList = dbmanager.getAwards(connection)
            return render_template('award.html', awardList = _awardList)

        if(request.form["action"] == "add_award_action"):
            dbmanager.addAward(request.form['add_desc'], request.form['add_last_winner_id'], connection)
            return redirect(url_for('award'))

        if(request.form["action"] == "delete_award_action"):
            dbmanager.deleteAward(request.form['id'], connection)
            return redirect(url_for('award'))

@app.route('/admin_panel/social_accounts', methods=['GET','POST'])
def social_accounts():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _socialAccountsList = dbmanager.getSocialAccounts(connection)
            return render_template('social_accounts.html', socialAccountsList = _socialAccountsList)

        if(request.form["action"] == "add_social_accounts_action"):
            dbmanager.addSocialAccountsList(request.form['add_twitter_account'], request.form['add_instagram_account'], request.form['add_facebook_account'], request.form['add_desc'], connection)
            return redirect(url_for('social_accounts'))

        if(request.form["action"] == "delete_social_accounts_action"):
            dbmanager.deleteSocialAccountsList(request.form['id'], connection)
            return redirect(url_for('social_accounts'))

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = "postgres://zzkyedon:gYzngQunejOWG5gmgjUbSJ-Xwr5lnPg-@jumbo.db.elephantsql.com:5432/zzkyedon"

    app.run(host='0.0.0.0', port=port, debug=debug)
