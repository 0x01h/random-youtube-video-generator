# Random YouTube Video Generator
Random YouTube video generator script using YouTube Data API v3 written in Python.

## Prerequisites
### Google Developer Key for YouTube

Sign up and change with your own developer key in the .env file: https://console.cloud.google.com/apis/credentials

`DEVELOPER_KEY = 'YOUR_DEVELOPER_KEY'`

### Google APIs Client Library

`pip3 install -r requirements.txt`

## Example Usage
`> random-youtube-video.py`

The output will be in the format "TITLE - https://www.youtube.com/watch?v=ID" :

`> IMG 4105 - https://www.youtube.com/watch?v=0CGyCMzi1l8`