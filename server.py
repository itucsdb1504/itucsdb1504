import datetime
import os

from flask import Flask
from flask import render_template
from players import Player

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())
@app.route('/players')
def players():
    player1 = {'name':'kerim'}
    player2 = {'name':'ahmet'}
    return render_template('players.html', player1=player1, player2=player2)



if __name__ == '__main__':
    PORT = int(os.getenv('VCAP_APP_PORT', '5000'))
    app.run(host='0.0.0.0', port=int(PORT))
