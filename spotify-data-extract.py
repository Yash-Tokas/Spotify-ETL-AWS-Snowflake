{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue255;\red45\green45\blue45;
\red0\green0\blue255;\red101\green76\blue29;\red0\green0\blue109;\red15\green112\blue1;\red0\green0\blue0;
\red144\green1\blue18;\red19\green118\blue70;\red32\green108\blue135;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c100000;\cssrgb\c23137\c23137\c23137;
\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c52549\c34510;\cssrgb\c14902\c49804\c60000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  json\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  os\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  spotipy\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  spotipy.oauth2 \cf2 \strokec2 import\cf4 \strokec4  SpotifyClientCredentials\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  boto3\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  datetime \cf2 \strokec2 import\cf4 \strokec4  datetime\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf4 \strokec4  \cf6 \strokec6 lambda_handler\cf4 \strokec4 (\cf7 \strokec7 event\cf4 \strokec4 , \cf7 \strokec7 context\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf8 \strokec8 # Retrieve Spotify API credentials from AWS Lambda environment variables\cf4 \cb1 \strokec4 \
\cb3     client_id \strokec9 =\strokec4  os.environ.get(\cf10 \strokec10 'client_id'\cf4 \strokec4 )\cb1 \
\cb3     client_secret \strokec9 =\strokec4  os.environ.get(\cf10 \strokec10 'client_secret'\cf4 \strokec4 )\cb1 \
\
\cb3     \cf8 \strokec8 # Authenticate with Spotify using Client Credentials Flow\cf4 \cb1 \strokec4 \
\cb3     client_credentials_manager \strokec9 =\strokec4  SpotifyClientCredentials(\cf7 \strokec7 client_id\cf4 \strokec9 =\strokec4 client_id, \cf7 \strokec7 client_secret\cf4 \strokec9 =\strokec4 client_secret)\cb1 \
\cb3     sp \strokec9 =\strokec4  spotipy.Spotify(\cf7 \strokec7 client_credentials_manager\cf4 \strokec9 =\strokec4 client_credentials_manager)\cb1 \
\cb3     playlists \strokec9 =\strokec4  sp.user_playlists(\cf10 \strokec10 '313odiyd72vqxinsh4grr4wqqfpa'\cf4 \strokec4 )  \cf8 \strokec8 # The user_playlists() function in the Spotipy library is used to retrieve a list of public playlists created by a specific Spotify user.\cf4 \cb1 \strokec4 \
\
\cb3     \cf8 \strokec8 # Define the Spotify playlist link and extract the playlist ID\cf4 \cb1 \strokec4 \
\cb3     playlist_link \strokec9 =\strokec4  \cf10 \strokec10 "https://open.spotify.com/playlist/34NbomaTu7YuOYnky8nLXL"\cf4 \cb1 \strokec4 \
\cb3     playlist_id \strokec9 =\strokec4  playlist_link.split(\cf10 \strokec10 "/"\cf4 \strokec4 )[\strokec9 -\cf11 \strokec11 1\cf4 \strokec4 ]\cb1 \
\
\cb3     data \strokec9 =\strokec4  sp.playlist_items(playlist_id) \cf8 \strokec8 # Fetch all items (tracks and details) from the specified playlist\cf4 \cb1 \strokec4 \
\
\cb3     client \strokec9 =\strokec4  boto3.client(\cf10 \strokec10 's3'\cf4 \strokec4 )  \cf8 \strokec8 # The boto3.client() function is used to create a low-level service client for interacting with AWS services.\cf4 \cb1 \strokec4 \
\
\cb3     filename \strokec9 =\strokec4  \cf10 \strokec10 "spotify_raw_"\cf4 \strokec4  \strokec9 +\strokec4  \cf12 \strokec12 str\cf4 \strokec4 (datetime.now()) \strokec9 +\strokec4  \cf10 \strokec10 ".json"\cf4 \strokec4   \cf8 \strokec8 # Generate a filename with a timestamp to ensure uniqueness\cf4 \cb1 \strokec4 \
\
\cb3     client.put_object(   \cf8 \strokec8 # The put_object() method is used to upload an object (file) to an Amazon S3 bucket.\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 Bucket\cf4 \strokec9 =\cf10 \strokec10 'snowflake-dw-project-yt'\cf4 \strokec4 ,    \cf8 \strokec8 # The name of the S3 bucket where the file will be uploaded.\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 Key\cf4 \strokec9 =\cf10 \strokec10 'spotify_ETL/raw_data/to_be_processed/'\cf4 \strokec4  \strokec9 +\strokec4  filename,    \cf8 \strokec8 # The name of the file in S3 (including the path, if needed).\cf4 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 Body\cf4 \strokec9 =\strokec4 json.dumps(data)    \cf8 \strokec8 # The actual data to be uploaded, converted to JSON format using json.dumps().\cf4 \cb1 \strokec4 \
\cb3     )\cb1 \
\
}