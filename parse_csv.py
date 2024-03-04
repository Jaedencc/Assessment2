import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('spotify_data.db')
cur = conn.cursor()

# Make sure that the old tables with the same name are removed before creating the new tables
conn.execute('DROP TABLE IF EXISTS spotify')
conn.execute('DROP TABLE IF EXISTS trackInformation')
print("table dropped successfully");

# create new tables
conn.execute('CREATE TABLE spotify (song_id INTEGER, key INTEGER, time_signature INTEGER, song_title TEXT, artist TEXT)')
print("table created successfully");

conn.execute('CREATE TABLE trackInformation (song_id INTEGER, song_title TEXT, acousticness REAL, danceability REAL, key INTEGER, mode INTEGER, FOREIGN KEY(song_id) REFERENCES spotify(song_id))')
print("trackInformation table created successfully")

# open the csv data file and read it into the database
with open('data_2024/spotify_data.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
# skip the header line
  next(reader)
  for row in reader:
    print(row)

    song_id = int(row[0])
    acousticness = float(row[1])
    danceability = float(row[2])
    key = int(row[6])
    mode = int(row[9])
    time_signature = int(row[12])
    song_title = row[15]
    artist = row[16]

    cur.execute('INSERT INTO spotify VALUES (?,?,?,?,?)', (song_id, key, time_signature, song_title, artist))
    
    cur.execute('INSERT INTO TrackInformation (song_id, song_title, acousticness, danceability, key, mode) VALUES (?, ?, ?, ?, ?, ?)', (song_id, song_title, acousticness, danceability, key, mode))
    
    conn.commit()

print("data parsed successfully");

conn.close()