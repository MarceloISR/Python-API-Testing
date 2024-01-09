import os

API_BASE_URL = os.environ["API_URL"]

API_KEY =  os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]


CONFIG_HEADERS = {
  'Authorization': f"Discogs key={API_KEY}, secret={API_SECRET}",
  'Content-Type': 'application/json'
}
# print("url:", API_BASE_URL)
# print("key:", API_KEY)
# print("secret:", API_SECRET)