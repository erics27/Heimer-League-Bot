import os
import requests
import json

key = str(os.environ.get("RIOT_API_KEY"))
user_input = input("What is your summoner name? ")
response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + user_input
                        + "?api_key=RGAPI-" + key)
user_data = json.loads(response.text)
name = user_data['name']
summoner_level = response.json()["summonerLevel"]
print(name + ": " + str(summoner_level))