# Random YouTube Video Generator
Random YouTube video generator script using YouTube Data API v3 written in Python. <br />
Due to its query parameter this script fetches low viewed (0 - 250 views) YouTube video IDs oftenly. <br /><br />
**Default Search Query:** `Prefix (IMG) + Random Integer (999-9999) + Postfix (MOV)` <br /><br />
You can change its parameter to whatever you want. <br />

## Prerequisites
**Google Developer Key for YouTube** <br />
`DEVELOPER_KEY = 'YOUR_DEVELOPER_KEY'` <br />
Sign up and change with your own developer key: https://console.developers.google.com <br /><br />
**Google APIs Client Library** <br />
`pip3 install --upgrade google-api-python-client`

## Example Usage
`> random-youtube-video.py` <br />
`> 0CGyCMzi1l8` <br /><br />
Now you can use this video ID as "https://www.youtube.com/watch?v=0CGyCMzi1l8" <br />
Change the ID parameter with your output: "https://www.youtube.com/watch?v=ID" <br /> 
