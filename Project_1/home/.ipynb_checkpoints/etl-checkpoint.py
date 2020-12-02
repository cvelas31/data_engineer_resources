import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import numpy as np

def nptypes2native(lista):
    """
    Transforms object types inside a list from numpy to native python
    
    Parameters:
    -----------
    lista : list(obj)
        List of different type of objects
    
    Return:
    -------
    new_lista : list(obj)
        New list with native python types
    """
    new_lista = []
    for element in lista:
        if hasattr(element, 'dtype'):
            if np.isnan(element):
                element = 'NaN'
            else:
                element = element.item()
        new_lista.append(element)
    return new_lista

def process_song_file(cur, filepath):
    """
    Process a song file and insert it into the corresponding tables (songs and artists tables)
    
    Parameters:
    -----------
    cur : cursor
        Cursor of postgres database
    filepath : str
        Path of the current file. Should be a json
        
    Return:
    -------
    None
    """
    df = pd.read_json(filepath, lines=True)

    columns_song = ['song_id', 'title', 'artist_id', 'year', 'duration']
    song_data = df.loc[0, columns_song].values.tolist()
    song_data = nptypes2native(song_data)   
    cur.execute(song_table_insert, song_data)
    
    columns_artist = ['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']
    artist_data = df.loc[0, columns_artist].values.tolist()
    artist_data = nptypes2native(artist_data)  
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Process a log file and insert it into the corresponding tables (users, time and songplays)
    
    Parameters:
    -----------
    cur : cursor
        Cursor of postgres database
    filepath : str
        Path of the current file. Should be a json
        
    Return:
    -------
    None
    """
    df = pd.read_json(filepath, lines=True)

    df = df[df['page']=='NextSong']

    df.loc[:,'ts'] = pd.to_datetime(df.ts, unit='ms')
    df['hour'] = df['ts'].dt.hour
    df['day'] = df['ts'].dt.day
    df['week'] = df['ts'].dt.week
    df['month'] = df['ts'].dt.month
    df['year'] = df['ts'].dt.year
    df['weekday'] = df['ts'].dt.weekday
    
    time_columns = ["ts", "hour", "day", "week", "month", "year", "weekday"]
    time_df = df[time_columns] 

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    columns_user = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_df = df[columns_user]

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Process data walking on a directory obtaining all the json files
    
    Parameters:
    -----------
    cur : cursor
        Cursor of postgres database
    conn : connection
        Connection to a postgres database
    filepath : str
        Path of the current file. Should be a json
    func : function
        Function to execute over files
        
    Return:
    -------
    None
    """
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()