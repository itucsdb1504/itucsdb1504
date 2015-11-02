import datetime
import os
import psycopg2

import dbmanager

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():

    '''if(dbmanager.isTableExists("public", "mytable")):
       print("OK")'''

    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/admin_panel/player')
def players():
    return render_template('player.html')


@app.route('/admin_panel')
def adminPage():
    return render_template('admin_panel.html')

@app.route('/admin_panel/news')
def addNews():
    return render_template('news.html')

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

@app.route('/admin_panel/sponsor')
def sponsor():
    return render_template('sponsor.html')

@app.route('/admin_panel/tournament')
def tournament():
    return render_template('tournament.html')

@app.route('/admin_panel/advertise')
def advertise():
    return render_template('advertise.html')

@app.route('/admin_panel/comment')
def comment():
    return render_template('comment.html')

@app.route('/admin_panel/user')
def user():
    return render_template('user.html')

@app.route('/admin_panel/venue')
def venue():
    if(dbmanager.isTableExists('public','venues') == False):
        dbmanager.createVenueTable()
        print("Venues Table Created!")
    else:
        print("Venues Table Already Exist!")

    return render_template('venue.html')

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
    app.run(host='0.0.0.0', port=port, debug=debug)