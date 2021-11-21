import os
import requests


response = requests.get("https://na1.api.riotgames.com/lol/status/v3/shard-data?api_key=RGAPI-")
output = response.json()
print(output)