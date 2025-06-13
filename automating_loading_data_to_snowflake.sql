{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 create or replace database spotify_ETL;\
\
create or replace schema spotify;\
\
// create the storage integration\
CREATE OR REPLACE STORAGE INTEGRATION s3_con\
TYPE = EXTERNAL_STAGE\
STORAGE_PROVIDER = 'S3'\
ENABLED = TRUE\
STORAGE_AWS_ROLE_ARN = '<arn_of_your_bucket>'\
STORAGE_ALLOWED_LOCATIONS = ('<your_bucket_location>')\
COMMENT = 'Creating connection to s3'\
\
// description of your storage\
DESC INTEGRATION s3_con;\
\
// create the tables you want\
create or replace table SPOTIFY_ETL.SPOTIFY.album (\
    album_id varchar(255),\
    album_name varchar(255),\
    release_date date,\
    total_tracks int,\
    url varchar(255)\
);\
\
create or replace table SPOTIFY_ETL.SPOTIFY.artists (\
    artist_id varchar(255),\
    artist_name varchar(255),\
    url varchar(255)\
);\
\
create or replace table SPOTIFY_ETL.SPOTIFY.songs (\
    song_id varchar(255),\
    song_name varchar(255),\
    duration_ms int,\
    url varchar(255),\
    popularity int,\
    song_added date,\
    album_id varchar(255),\
    artist_id varchar(255)\
);\
\
// create the file format\
create or replace file format SPOTIFY_ETL.SPOTIFY.csv_format\
    type = csv\
    field_delimiter = ','\
    skip_header = 1\
    null_if = ('NULL', 'null')\
    empty_field_as_null = TRUE\
    field_optionally_enclosed_by = '"';\
\
// prepare the stage for your data.\
create or replace stage SPOTIFY_ETL.SPOTIFY.album_csv_stage\
    url = 's3://snowflake-dw-project-yt/spotify_ETL/transformed_data/album_data/'\
    STORAGE_INTEGRATION = s3_con\
    file_format = SPOTIFY_ETL.SPOTIFY.csv_format\
\
create or replace stage SPOTIFY_ETL.SPOTIFY.artist_csv_stage\
    url = 's3://snowflake-dw-project-yt/spotify_ETL/transformed_data/artist_data/'\
    STORAGE_INTEGRATION = s3_con\
    file_format = SPOTIFY_ETL.SPOTIFY.csv_format\
\
create or replace stage SPOTIFY_ETL.SPOTIFY.songs_csv_stage\
    url = 's3://snowflake-dw-project-yt/spotify_ETL/transformed_data/songs_data/'\
    STORAGE_INTEGRATION = s3_con\
    file_format = SPOTIFY_ETL.SPOTIFY.csv_format\
\
// create the snowpipe for automating the data transfer to the tables you created in snowflake\
create or replace pipe SPOTIFY_ETL.SPOTIFY.album_pipe\
    auto_ingest = TRUE\
    as\
    copy into SPOTIFY_ETL.SPOTIFY.album\
    from @SPOTIFY_ETL.SPOTIFY.album_csv_stage\
\
create or replace pipe SPOTIFY_ETL.SPOTIFY.artist_pipe\
    auto_ingest = TRUE\
    as\
    copy into SPOTIFY_ETL.SPOTIFY.artists\
    from @SPOTIFY_ETL.SPOTIFY.artist_csv_stage\
\
create or replace pipe SPOTIFY_ETL.SPOTIFY.songs_pipe\
    auto_ingest = TRUE\
    as\
    copy into SPOTIFY_ETL.SPOTIFY.songs\
    from @SPOTIFY_ETL.SPOTIFY.songs_csv_stage\
\
    // description of the pipe\
desc pipe SPOTIFY_ETL.SPOTIFY.album_pipe;\
\
desc pipe SPOTIFY_ETL.SPOTIFY.artist_pipe;\
\
desc pipe SPOTIFY_ETL.SPOTIFY.songs_pipe;\
\
// you can start querying your tables.\
select * from album;\
\
select * from artists;\
\
select * from songs;}