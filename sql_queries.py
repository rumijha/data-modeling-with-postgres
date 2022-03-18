# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
songplay_id serial PRIMARY KEY,
start_time bigint not null, 
user_id int not null, 
level varchar not null,
song_id varchar, 
artist_id varchar, 
session_id int, 
location varchar, 
user_agent varchar,
UNIQUE (start_time, user_id));
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id int PRIMARY KEY, 
first_name varchar not null, 
last_name varchar not null, 
gender varchar, 
level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
song_id varchar PRIMARY KEY, 
title varchar not null, 
artist_id varchar not null, 
year int, 
duration numeric not null);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
artist_id varchar PRIMARY KEY, 
name varchar not null, 
location varchar, 
latitude numeric,
longitude numeric);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time bigint PRIMARY KEY, 
hour int not null, 
day int not null, 
week int not null, 
month int not null, 
year int not null, 
weekday int not null);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays 
(start_time, user_id, level, song_id, 
artist_id, session_id, location, user_agent)
values(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users 
(user_id, first_name, last_name, gender, level)
values(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs 
(song_id, title, artist_id, year, duration)
values(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING ;
""")

artist_table_insert = ("""
INSERT INTO artists 
(artist_id, name, location, latitude, longitude)
values(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time 
(start_time, hour, day, week, 
month, year, weekday)
values(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT song_id, a.artist_id FROM songs s
join artists a on s.artist_id = a.artist_id
where s.title = %s and a.name = %s and s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]