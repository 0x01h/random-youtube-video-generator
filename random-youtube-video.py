import random, os, json, string
from dotenv import load_dotenv
from googleapiclient.discovery import build_from_document

load_dotenv()

DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
  
def youtube_search():
  with open("service.json", encoding="utf-8") as f:
    service = json.load(f)
    
  youtube = build_from_document(service, developerKey=DEVELOPER_KEY)

  z = ""
  for x in range(0, random.randint(1, 7)):
    y = random.choice([char for char in string.printable])
    z = z + y

  search_response = youtube.search().list(
    q=str(z),
    part="snippet",
    maxResults=5
  ).execute()

  videosId = []
  videosTitle=[]

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videosId.append("%s" % (search_result["id"]["videoId"]))
      videosTitle.append(search_result["snippet"]["title"])

  index = random.randint(0, 2)
  return [videosId[index], videosTitle[index]]

video = youtube_search()

print(f"{video[1]} - https://www.youtube.com/watch?v={video[0]}")
