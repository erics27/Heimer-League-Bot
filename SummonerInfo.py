import os
import requests
import json


class SummonerInfo:

    key = str(os.environ.get("RIOT_API_KEY"))
    summoner_name = ""
    no_spaces_summoner_name = ""
    puuid = ""
    match_history = []

    def __int__(self, sum_name):
        self.summoner_name = sum_name
        self.no_spaces_summoner_name = sum_name.replace(" ", "%20")
        self.puuid = self.get_puuid()

    def get_puuid(self):
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
                                + self.no_spaces_summoner_name + "?api_key=RGAPI-" + self.key)
        return response.json()['puuid']

    def get_level(self):
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
                                + self.no_spaces_summoner_name + "?api_key=RGAPI-" + self.key)
        user_data = json.loads(response.text)
        name = str(user_data['name'])
        summoner_level = str(response.json()['summonerLevel'])
        print(name + ": " + str(summoner_level))
        return [name, summoner_level]
    
