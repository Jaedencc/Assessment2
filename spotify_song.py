import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db_name = 'spotify_data.db'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/song_details')
def song_details():
  #open the connection to the spotify database
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from spotify")
  rows = cur.fetchall()
  conn.close()
  return render_template('song_details.html', rows=rows)

@app.route('/track_information')
def track_information():
  #open the connection to the spotify database
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from trackInformation")
  rows = cur.fetchall()
  conn.close()
  return render_template('track_information.html', rows=rows)

@app.route('/favorite_songs')
def favorite_songs():
  #open the connection to the spotify database
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from trackInformation")
  rows = cur.fetchall()
  conn.close()
  return render_template('favorite_songs.html', rows=rows)