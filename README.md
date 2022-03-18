# Project description
I have created a database for a startup company called Sparkify. It is a music streaming app that holds every detail of a song like- songTitle, artistName, songDuration, location, etc. I have built ETL pipelines wherein the raw data are processed, normalized, and stored in tables. Storing data in the normalized form helps users to retrieve the data quickly as there is no inconsistency or redundant data available. The resultant output is optimized and can be utilized by data scientists for analysis and decision-making purposes.

**Database Design**\
Created a STAR schema for databse Sparkify.\
Fact Table: songplays: attributes referencing to the dimension tables.\
Dimension Tables: users, songs, artists and time table.

**ETL Process**\
created and inserted records into songs, artist dimension tables from extracting records from songs_data files.\
created and inserted records into users, time dimension tabless from extracting records from log_data files.\
Created fact table from the dimensison tables and log_data called songplays.


**Project Repository files**\
songs_data files for inserting records into songs, artist dimension tables.\
log_data files for inserting records into users, time dimension tables.


**How To Run the Project**\
Steps to run and implement the database successfully are as below:\
Step1: Run Create_Table.py script which make use of sql_queries.py to Create, Insert, Drop, and Select the database and tables.\
Step2: Implement etl.ipynb which processes single file and inserts record into each table created under sql_queries.py\
Step3: You can use test.ipynb to check if records are inserted into each table\
step4: Run etl.py to process all the files under given path and insert the records into respective tables\
Step5: You can again use test.ipynb to check if all the records are inserted into respective tables.

