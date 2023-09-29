import json
import sqlite3

conn = sqlite3.connect('spotify.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    artist_id  INTEGER,
    msPlayed INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) :
    fname = 'StreamingHistory0.json'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
str_data = open(fname,encoding="utf-8").read()
json_data = json.loads(str_data)

for entry in json_data:
    artist=entry['artistName']
    title=entry['trackName']
    msPlayed=entry['msPlayed']
    print(artist,title,msPlayed)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    #cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    #artist_id = cur.fetchone()[0]

    #cur.execute('''INSERT OR REPLACE INTO Track
        #(title, artist_id, msPlayed)
        #VALUES ( ?, ?, ?)''',
        #( title, artist_id, msPlayed) )


    conn.commit()
