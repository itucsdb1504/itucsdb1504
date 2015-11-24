import datetime
import psycopg2 as dbapi2
import json
import os
import re
import logging

import dbmanager

from flask import Flask
from flask import render_template
from flask import redirect
from flask.helpers import url_for
from flask import request

app = Flask(__name__)


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

    '''if(dbmanager.isTableExists("public", "mytable")):
       print("OK")'''

    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())


@app.route('/admin_panel')
def adminPage():
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


@app.route('/admin_panel/record')
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

@app.route('/admin_panel/video')
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

@app.route('/admin_panel/match')
def addMatch():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _matchList = dbmanager.getMathes(connection)
            return render_template('match.html', matchList = _matchList)

        if(request.form["action"] == "add_match_action"):
            dbmanager.addMatch(request.form['add_tournamentName'], request.form['add_venueName'], request.form['add_player1'],request.form['add_player2'], request.form['add_isLive'], request.form['add_score'],connection)
            return redirect(url_for('addMatch'))

        if(request.form["action"] == "delete_match_action"):
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

@app.route('/admin_panel/tournament')
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


@app.route('/admin_panel/advertise')
def advertise():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _advertiseList = dbmanager.getAdvertises(connection)
            return render_template('advertise.html', advertiseList = _advertiseList)

        if(request.form["action"] == "add_advertise_action"):
            dbmanager.addSponsor(request.form['advertise_imageurl'], request.form['advertise_exturl'], request.form['advertise_size'], connection)
            return redirect(url_for('advertise'))

        if(request.form["action"] == "delete_advertise_action"):
            dbmanager.deleteSponsor(request.form['id'], connection)
            return redirect(url_for('advertise'))

        return render_template('advertise.html')

@app.route('/admin_panel/comment', methods=['GET','POST'])
def comment():

    if(request.method == 'GET'):
        _commentList = dbmanager.getComments("null")
        return render_template('comment.html', commentList = _commentList)

    if(request.form["action"] == "add_comment_action"):
        dbmanager.addComment(request.form['comment_username'], request.form['comment_title'], request.form['comment_content'], request.form['comment_date'])
        return redirect(url_for('comment'))

    if(request.form["action"] == "delete_comment_action"):
        dbmanager.deleteComment(request.form['id'])
        return redirect(url_for('comment'))

@app.route('/admin_panel/user')
def user():
    return render_template('user.html')

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

@app.route('/admin_panel/ticket')
def ticket():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _ticketList = dbmanager.getTickets(connection)
            return render_template('ticket.html', matchList = _matchList)

        if(request.form["action"] == "add_ticket_action"):
            dbmanager.addTicket(request.form['add_ticket_venue'], request.form['add_ticket_title'], request.form['add_ticket_content'],request.form['add_ticket_price'], request.form['add_ticket_exturl'], request.form['add_ticket_date'],connection)
            return redirect(url_for('ticket'))

        if(request.form["action"] == "delete_ticket_action"):
            dbmanager.deleteTicket(request.form['id'], connection)
            return redirect(url_for('ticket'))

        return render_template('ticket.html')

@app.route('/admin_panel/channel')
def channel():
    with dbapi2.connect(app.config['dsn']) as connection:
        if(request.method == 'GET'):
            _channelList = dbmanager.getChannels(connection)
            return render_template('channel.html', channelList = _channelList)

        if(request.form["action"] == "add_channel_action"):
            dbmanager.addChannel(request.form['add_channel_name'], request.form['add_channel_imageurl'], request.form['add_channel_exturl'], connection)
            return redirect(url_for('channel'))

        if(request.form["action"] == "delete_channel_action"):
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
        app.config['dsn'] = """host='localhost' port='5432' dbname='postgres' user='postgres' password='Abcd1234'"""

    app.run(host='0.0.0.0', port=port, debug=debug)
