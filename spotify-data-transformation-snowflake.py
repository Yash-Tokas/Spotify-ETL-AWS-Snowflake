{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue255;\red45\green45\blue45;
\red15\green112\blue1;\red0\green0\blue255;\red101\green76\blue29;\red0\green0\blue109;\red0\green0\blue0;
\red144\green1\blue18;\red19\green118\blue70;\red32\green108\blue135;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c100000;\cssrgb\c23137\c23137\c23137;
\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c52549\c34510;\cssrgb\c14902\c49804\c60000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  json  \cf5 \strokec5 # Import JSON module to handle JSON data\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  boto3  \cf5 \strokec5 # Import Boto3 to interact with AWS services (S3)\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  datetime \cf2 \strokec2 import\cf4 \strokec4  datetime  \cf5 \strokec5 # Import datetime to generate timestamps\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  io \cf2 \strokec2 import\cf4 \strokec4  StringIO  \cf5 \strokec5 # Import StringIO to handle CSV in-memory operations\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  pandas \cf2 \strokec2 as\cf4 \strokec4  pd  \cf5 \strokec5 # Import Pandas for data manipulation\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 album\cf4 \strokec4 (\cf8 \strokec8 data\cf4 \strokec4 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     album_list \strokec9 =\strokec4  []  \cf5 \strokec5 # Initialize an empty list to store album details\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 for\cf4 \strokec4  row \cf2 \strokec2 in\cf4 \strokec4  data[\cf10 \strokec10 'items'\cf4 \strokec4 ]:  \cf5 \strokec5 # Iterate over all songs in the playlist\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_id \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'album'\cf4 \strokec4 ][\cf10 \strokec10 'id'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract album ID\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_name \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'album'\cf4 \strokec4 ][\cf10 \strokec10 'name'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract album name\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_release_date \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'album'\cf4 \strokec4 ][\cf10 \strokec10 'release_date'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract release date\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_total_tracks \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'album'\cf4 \strokec4 ][\cf10 \strokec10 'total_tracks'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract total tracks in the album\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_url \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'album'\cf4 \strokec4 ][\cf10 \strokec10 'external_urls'\cf4 \strokec4 ][\cf10 \strokec10 'spotify'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract album Spotify URL\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         album_elements \strokec9 =\strokec4  \{  \cf5 \strokec5 # Store album details in a dictionary\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'album_id'\cf4 \strokec4 : album_id, \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'name'\cf4 \strokec4 : album_name, \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'release_date'\cf4 \strokec4 : album_release_date, \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'total_tracks'\cf4 \strokec4 : album_total_tracks, \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'url'\cf4 \strokec4 : album_url\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \}\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         album_list.append(album_elements)  \cf5 \strokec5 # Append album dictionary to list\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 return\cf4 \strokec4  album_list  \cf5 \strokec5 # Return list of album details\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 artist\cf4 \strokec4 (\cf8 \strokec8 data\cf4 \strokec4 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     artist_list \strokec9 =\strokec4  []  \cf5 \strokec5 # Initialize an empty list to store artist details\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 for\cf4 \strokec4  row \cf2 \strokec2 in\cf4 \strokec4  data[\cf10 \strokec10 'items'\cf4 \strokec4 ]:  \cf5 \strokec5 # Iterate over all songs in the playlist\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf2 \strokec2 for\cf4 \strokec4  key, value \cf2 \strokec2 in\cf4 \strokec4  row.items():  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf2 \strokec2 if\cf4 \strokec4  key \strokec9 ==\strokec4  \cf10 \strokec10 'track'\cf4 \strokec4 :  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                 \cf2 \strokec2 for\cf4 \strokec4  artist \cf2 \strokec2 in\cf4 \strokec4  value[\cf10 \strokec10 'artists'\cf4 \strokec4 ]:  \cf5 \strokec5 # Loop through all artists in a song\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                     artist_dict \strokec9 =\strokec4  \{  \cf5 \strokec5 # Store artist details in a dictionary\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                         \cf10 \strokec10 'artist_id'\cf4 \strokec4 : artist[\cf10 \strokec10 'id'\cf4 \strokec4 ],  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                         \cf10 \strokec10 'name'\cf4 \strokec4 : artist[\cf10 \strokec10 'name'\cf4 \strokec4 ],  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                         \cf10 \strokec10 'url'\cf4 \strokec4 : artist[\cf10 \strokec10 'href'\cf4 \strokec4 ]\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4                     \}  \cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4                     artist_list.append(artist_dict)  \cf5 \strokec5 # Append artist dictionary to list\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 return\cf4 \strokec4  artist_list  \cf5 \strokec5 # Return list of artist details\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 songs\cf4 \strokec4 (\cf8 \strokec8 data\cf4 \strokec4 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     song_list \strokec9 =\strokec4  []  \cf5 \strokec5 # Initialize an empty list to store song details\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 for\cf4 \strokec4  row \cf2 \strokec2 in\cf4 \strokec4  data[\cf10 \strokec10 'items'\cf4 \strokec4 ]:  \cf5 \strokec5 # Iterate over all songs in the playlist\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_id \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'id'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract song ID\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_name \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'name'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract song name\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_duration \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'duration_ms'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract song duration in milliseconds\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_url \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'external_urls'\cf4 \strokec4 ][\cf10 \strokec10 'spotify'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract song Spotify URL\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_popularity \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'popularity'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract song popularity score\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_added \strokec9 =\strokec4  row[\cf10 \strokec10 'added_at'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract timestamp when song was added\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_id \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'album'\cf4 \strokec4 ][\cf10 \strokec10 'id'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract album ID of the song\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         artist_id \strokec9 =\strokec4  row[\cf10 \strokec10 'track'\cf4 \strokec4 ][\cf10 \strokec10 'album'\cf4 \strokec4 ][\cf10 \strokec10 'artists'\cf4 \strokec4 ][\cf11 \strokec11 0\cf4 \strokec4 ][\cf10 \strokec10 'id'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract first artist's ID\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         song_element \strokec9 =\strokec4  \{  \cf5 \strokec5 # Store song details in a dictionary\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'song_id'\cf4 \strokec4 : song_id,  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'song_name'\cf4 \strokec4 : song_name,  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'duration_ms'\cf4 \strokec4 : song_duration,  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'url'\cf4 \strokec4 : song_url,  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'popularity'\cf4 \strokec4 : song_popularity,  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'song_added'\cf4 \strokec4 : song_added,  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'album_id'\cf4 \strokec4 : album_id,  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'artist_id'\cf4 \strokec4 : artist_id  \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \}  \cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         song_list.append(song_element)  \cf5 \strokec5 # Append song dictionary to list\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 return\cf4 \strokec4  song_list  \cf5 \strokec5 # Return list of song details\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf4 \strokec4  \cf7 \strokec7 lambda_handler\cf4 \strokec4 (\cf8 \strokec8 event\cf4 \strokec4 , \cf8 \strokec8 context\cf4 \strokec4 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 \strokec4     s3 \strokec9 =\strokec4  boto3.client(\cf10 \strokec10 's3'\cf4 \strokec4 )  \cf5 \strokec5 # Initialize an S3 client to interact with S3\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     bucket \strokec9 =\strokec4  \cf10 \strokec10 "snowflake-dw-project-yt"\cf4 \strokec4   \cf5 \strokec5 # Define the bucket name\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     key \strokec9 =\strokec4  \cf10 \strokec10 "spotify_ETL/raw_data/to_be_processed/"\cf4 \strokec4   \cf5 \strokec5 # Define the folder where JSON files are stored\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     spotify_data \strokec9 =\strokec4  []  \cf5 \strokec5 # Initialize list to store JSON data\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     spotify_keys \strokec9 =\strokec4  []  \cf5 \strokec5 # Initialize list to store processed file keys\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     \cf2 \strokec2 for\cf4 \strokec4  \strokec9 file\strokec4  \cf2 \strokec2 in\cf4 \strokec4  s3.list_objects(\cf8 \strokec8 Bucket\cf4 \strokec9 =\strokec4 bucket, \cf8 \strokec8 Prefix\cf4 \strokec9 =\strokec4 key)[\cf10 \strokec10 'Contents'\cf4 \strokec4 ]:  \cf5 \strokec5 # List all objects in S3 under the specified prefix\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         file_key \strokec9 =\strokec4  \strokec9 file\strokec4 [\cf10 \strokec10 'Key'\cf4 \strokec4 ]  \cf5 \strokec5 # Extract file name (key)\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \cf2 \strokec2 if\cf4 \strokec4  file_key.split(\cf10 \strokec10 '.'\cf4 \strokec4 )[\strokec9 -\cf11 \strokec11 1\cf4 \strokec4 ] \strokec9 ==\strokec4  \cf10 \strokec10 "json"\cf4 \strokec4 :  \cf5 \strokec5 # Check if the file is a JSON file\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             response \strokec9 =\strokec4  s3.get_object(\cf8 \strokec8 Bucket\cf4 \strokec9 =\strokec4 bucket, \cf8 \strokec8 Key\cf4 \strokec9 =\strokec4 file_key)  \cf5 \strokec5 # Fetch the file from S3\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             content \strokec9 =\strokec4  response[\cf10 \strokec10 'Body'\cf4 \strokec4 ]  \cf5 \strokec5 # Read the content of the file\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             jsonObject \strokec9 =\strokec4  json.loads(content.read())  \cf5 \strokec5 # Convert JSON data into a Python dictionary\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             spotify_data.append(jsonObject)  \cf5 \strokec5 # Store extracted JSON data\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             spotify_keys.append(file_key)  \cf5 \strokec5 # Store processed file key\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf2 \strokec2 for\cf4 \strokec4  data \cf2 \strokec2 in\cf4 \strokec4  spotify_data:  \cf5 \strokec5 # Process each JSON dataset\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_list \strokec9 =\strokec4  album(data)  \cf5 \strokec5 # Extract album details\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         artist_list \strokec9 =\strokec4  artist(data)  \cf5 \strokec5 # Extract artist details\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_list \strokec9 =\strokec4  songs(data)  \cf5 \strokec5 # Extract song details\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         album_df \strokec9 =\strokec4  pd.DataFrame.from_dict(album_list)  \cf5 \strokec5 # Convert album list to a Pandas DataFrame\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_df \strokec9 =\strokec4  album_df.drop_duplicates(\cf8 \strokec8 subset\cf4 \strokec9 =\strokec4 [\cf10 \strokec10 'album_id'\cf4 \strokec4 ])  \cf5 \strokec5 # Remove duplicate albums\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_df[\cf10 \strokec10 'release_date'\cf4 \strokec4 ] \strokec9 =\strokec4  pd.to_datetime(album_df[\cf10 \strokec10 'release_date'\cf4 \strokec4 ])  \cf5 \strokec5 # Convert release date to datetime\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         artist_df \strokec9 =\strokec4  pd.DataFrame.from_dict(artist_list)  \cf5 \strokec5 # Convert artist list to a Pandas DataFrame\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         artist_df \strokec9 =\strokec4  artist_df.drop_duplicates(\cf8 \strokec8 subset\cf4 \strokec9 =\strokec4 [\cf10 \strokec10 'artist_id'\cf4 \strokec4 ])  \cf5 \strokec5 # Remove duplicate artists\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         song_df \strokec9 =\strokec4  pd.DataFrame.from_dict(song_list)  \cf5 \strokec5 # Convert song list to a Pandas DataFrame\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_df \strokec9 =\strokec4  song_df.drop_duplicates(\cf8 \strokec8 subset\cf4 \strokec9 =\strokec4 [\cf10 \strokec10 'song_id'\cf4 \strokec4 ])  \cf5 \strokec5 # Remove duplicate songs\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_df[\cf10 \strokec10 'song_added'\cf4 \strokec4 ] \strokec9 =\strokec4  pd.to_datetime(song_df[\cf10 \strokec10 'song_added'\cf4 \strokec4 ])  \cf5 \strokec5 # Convert song added timestamp to datetime\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         song_key \strokec9 =\strokec4  \cf10 \strokec10 "spotify_ETL/transformed_data/songs_data/song_transformed_"\cf4 \strokec4  \strokec9 +\strokec4  \cf12 \strokec12 str\cf4 \strokec4 (datetime.now()) \strokec9 +\strokec4  \cf10 \strokec10 ".csv"\cf4 \strokec4   \cf5 \strokec5 # Define the transformed song file path\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_buffer \strokec9 =\strokec4  StringIO()  \cf5 \strokec5 # Create an in-memory buffer for the CSV file\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_df.to_csv(song_buffer, \cf8 \strokec8 index\cf4 \strokec9 =\cf6 \strokec6 False\cf4 \strokec4 )  \cf5 \strokec5 # Convert DataFrame to CSV format, and not have a seprate index column\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         song_content \strokec9 =\strokec4  song_buffer.getvalue()  \cf5 \strokec5 # Retrieve CSV data as a string\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         s3.put_object(\cf8 \strokec8 Bucket\cf4 \strokec9 =\strokec4 bucket, \cf8 \strokec8 Key\cf4 \strokec9 =\strokec4 song_key, \cf8 \strokec8 Body\cf4 \strokec9 =\strokec4 song_content)  \cf5 \strokec5 # Upload the transformed song data to S3\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         artist_key \strokec9 =\strokec4  \cf10 \strokec10 "spotify_ETL/transformed_data/artist_data/artist_transformed_"\cf4 \strokec4  \strokec9 +\strokec4  \cf12 \strokec12 str\cf4 \strokec4 (datetime.now()) \strokec9 +\strokec4  \cf10 \strokec10 ".csv"\cf4 \strokec4   \cf5 \strokec5 # Define the transformed artist file path\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         artist_buffer \strokec9 =\strokec4  StringIO()  \cf5 \strokec5 # Create an in-memory buffer for the CSV file\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         artist_df.to_csv(artist_buffer, \cf8 \strokec8 index\cf4 \strokec9 =\cf6 \strokec6 False\cf4 \strokec4 )  \cf5 \strokec5 # Convert DataFrame to CSV format, and not have a seprate index column\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         artist_content \strokec9 =\strokec4  artist_buffer.getvalue()  \cf5 \strokec5 # Retrieve CSV data as a string\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         s3.put_object(\cf8 \strokec8 Bucket\cf4 \strokec9 =\strokec4 bucket, \cf8 \strokec8 Key\cf4 \strokec9 =\strokec4 artist_key, \cf8 \strokec8 Body\cf4 \strokec9 =\strokec4 artist_content)  \cf5 \strokec5 # Upload the transformed artist data to S3\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4         album_key \strokec9 =\strokec4  \cf10 \strokec10 "spotify_ETL/transformed_data/album_data/album_transformed_"\cf4 \strokec4  \strokec9 +\strokec4  \cf12 \strokec12 str\cf4 \strokec4 (datetime.now()) \strokec9 +\strokec4  \cf10 \strokec10 ".csv"\cf4 \strokec4   \cf5 \strokec5 # Define the transformed album file path\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_buffer \strokec9 =\strokec4  StringIO()  \cf5 \strokec5 # Create an in-memory buffer for the CSV file\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_df.to_csv(album_buffer, \cf8 \strokec8 index\cf4 \strokec9 =\cf6 \strokec6 False\cf4 \strokec4 )  \cf5 \strokec5 # Convert DataFrame to CSV format, and not have a seprate index column\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         album_content \strokec9 =\strokec4  album_buffer.getvalue()  \cf5 \strokec5 # Retrieve CSV data as a string\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         s3.put_object(\cf8 \strokec8 Bucket\cf4 \strokec9 =\strokec4 bucket, \cf8 \strokec8 Key\cf4 \strokec9 =\strokec4 album_key, \cf8 \strokec8 Body\cf4 \strokec9 =\strokec4 album_content)  \cf5 \strokec5 # Upload the transformed album data to S3\cf4 \cb1 \strokec4 \
\
\cf4 \cb3 \strokec4     s3_resource \strokec9 =\strokec4  boto3.resource(\cf10 \strokec10 's3'\cf4 \strokec4 )  \cf5 \strokec5 # Initialize an S3 resource to manage objects\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4     \cf2 \strokec2 for\cf4 \strokec4  key \cf2 \strokec2 in\cf4 \strokec4  spotify_keys:  \cf5 \strokec5 # Iterate over processed files\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         copy_source \strokec9 =\strokec4  \{  \cf5 \strokec5 # Define the source file for copying\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'Bucket'\cf4 \strokec4 : bucket,\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4             \cf10 \strokec10 'Key'\cf4 \strokec4 : key\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         \}\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         s3_resource.meta.client.copy(copy_source, bucket, \cf10 \strokec10 "spotify_ETL/raw_data/processed/"\cf4 \strokec4  \strokec9 +\strokec4  key.split(\cf10 \strokec10 '/'\cf4 \strokec4 )[\strokec9 -\cf11 \strokec11 1\cf4 \strokec4 ])  \cf5 \strokec5 # Copy file to processed folder\cf4 \cb1 \strokec4 \
\cf4 \cb3 \strokec4         s3_resource.Object(bucket, key).delete()  \cf5 \strokec5 # Delete the original file from "to_be_processed" folder\cf4 \cb1 \strokec4 \
\
}