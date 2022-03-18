import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *



def process_song_file(cur, filepath):
    """"
    This procedure processes a song_data file.
    It extracts the song information in order to store it into the songs table.
    Then it extracts the artist information in order to store it into the artists table.

    INPUTS: 
    * cur: Cusrsor allows python to process sql queries and fetch results
    * filepath: Path to the song_data file
    """
    # open song file
    df = pd.read_json(filepath, typ='dictionary')

    # insert song record
    song_data = df.values[[6,7,1,9,8]]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df.values[[1,5,4,2,3]]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """"
    This procedure processes a log_data file.
    It extracts the log information in order to store it into the user table.
    Then it extracts the time information in order to store it into the time table.
    Finallt it extracts the artists and song information to store it into the songplay table.

    INPUTS: 
    * cur: Cusrsor allows python to process sql queries and fetch results
    * filepath: Path to the log_data file
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = [df.ts, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday]
    column_labels = ['timestamp', 'hour', 'day', 'weekofyear', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(data = dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """"
    Process all the files present for song_data and log_data.

    INPUTS: 
    * Connection: Provided connection details to connect to the database
    * cur: Cusrsor allows python to Cusrsor allows python to process sql queries and fetch results
    * filepath: Path to the song_data and log_data file
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """" 
    * Connection: Provided connection details to connect to the database
    * cur: Cusrsor allows python to process sql queries and fetch results
    * filepath: Path to the song_data and log_data files
    * Process both song_data and log_data
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()