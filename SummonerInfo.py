import os
import requests

key = str(os.environ.get("RIOT_API_KEY"))
response = requests.get("https://na1.api.riotgames.com/lol/status/v3/shard-data?api_key=RGAPI-" + key)
output = response.json()
