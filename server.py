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

@app.route('/admin_panel/player')
def player():
    if(request.method == 'GET'):
        _playerList = dbmanager.getPlayer()
        return render_template('player.html', playerList = _playerList)

    if(request.form["action"] == "add_player_action"):
        dbmanager.addPlayer(request.form['add_name'], request.form['add_imageURL'], request.form['add_extURL'])
        return redirect(url_for('player'))


@app.route('/admin_panel')
def adminPage():
    return render_template('admin_panel.html')

@app.route('/admin_panel/news', methods=['GET','POST'])
def addNews():
    if(request.method == 'GET'):
        _newsList = dbmanager.getNews()
        return render_template('news.html', newsList = _newsList)

    if(request.form["action"] == "add_news_action"):
        dbmanager.addNews(request.form['news_title'], request.form['message'], request.form['news_imageurl'], request.form['news_date'])
        return redirect(url_for('addNews'))

    if(request.form["action"] == "delete_news_action"):
        dbmanager.deleteNews(request.form['id'])
        return redirect(url_for('addNews'))


@app.route('/admin_panel/test')
def testHtml():
    return render_template('test.html')

@app.route('/admin_panel/record')
def addRecord():
    return render_template('record.html')

@app.route('/admin_panel/video')
def addVideo():
    return render_template('video.html')

@app.route('/admin_panel/match')
def addMatch():
    return render_template('match.html')

@app.route('/admin_panel/sponsor', methods=['GET','POST'])
def sponsor():
    if(request.method == 'GET'):
        _sponsorList = dbmanager.getSponsor()
        return render_template('sponsor.html', sponsorList = _sponsorList)

    if(request.form["action"] == "add_sponsor_action"):
        dbmanager.addSponsor(request.form['add_name'], request.form['add_imageURL'], request.form['add_extURL'])
        return redirect(url_for('sponsor'))

    if(request.form["action"] == "delete_sponsor_action"):
        dbmanager.deleteSponsor(request.form['id'])
        return redirect(url_for('sponsor'))

@app.route('/admin_panel/tournament')
def tournament():
    return render_template('tournament.html')

@app.route('/admin_panel/advertise')
def advertise():
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
            dbmanager.addVenue(request.form['add_name'], request.form['add_capacity'], request.form['add_location'], request.form['add_desc'])
            return redirect(url_for('venue'))

        if(request.form["action"] == "delete_venue_action"):
            print("DELETE")
            dbmanager.deleteVenue(request.form['id'])
            return redirect(url_for('venue'))


@app.route('/admin_panel/ticket')
def ticket():
    return render_template('ticket.html')

@app.route('/admin_panel/channel')
def channel():
    return render_template('channel.html')

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
        app.config['dsn'] = """user='vagrant' password='vagrant' host='localhost' port=54321 dbname='itucsdb'"""

    app.run(host='0.0.0.0', port=port, debug=debug)