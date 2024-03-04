from behave import given, when, then
import sqlite3

@given(u'the Spotify table is created')
def create_table(context):
  context.conn = sqlite3.connect('spotify_data.db')
  context.cur = context.conn.cursor()
  context.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='spotify'")
  result = context.cur.fetchall()
#If the spotify table exists, the list length is not equal to 0
  assert len(result) != 0, "Table 'spotify' was not created"
  context.conn.commit()

@when(u'I insert a data row into the Spotify table')
def insert_data(context):
  context.test_data = (2024, 1, 1, 'Test SongName', 'Test ArtistName')
  context.cur.execute('INSERT INTO spotify VALUES (?,?,?,?,?)', context.test_data)
  context.conn.commit()

@then(u'the data should be queried from the Spotify table')
def query_data(context):
  context.cur.execute('SELECT * FROM spotify WHERE song_id=2024')
  data = context.cur.fetchall()
#Use print() to aid debugging, if queried data is not same with inserted data, show the detail of both data.
  print(data)
  print(context.test_data)
  assert data, "Data was not inserted"
  assert context.test_data in data, "Inserted data does not match"
  context.cur.execute('DELETE FROM spotify WHERE song_id=2024')
  context.conn.commit()
  context.conn.close()
