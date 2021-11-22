import os
import requests
import json


class SummonerInfo:

    key = str(os.environ.get("RIOT_API_KEY"))
    summoner_name = ""
    no_spaces_summoner_name = ""
    puuid = ""
    match_id_history = []

    def __int__(self, sum_name):
        self.summoner_name = sum_name
        self.no_spaces_summoner_name = sum_name.replace(" ", "%20")
        self.puuid = self.get_puuid()
        self.match_id_history = self.get_match_id_history()

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

    def get_match_id_history(self):
        response = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"
                                + self.puuid + "/ids?start=0&count=20&api_key=RGAPI-" + self.key)
        match_list = json.loads(response.text)
        return match_list

    def get_most_recent_match_info(self):
        recent_match_id = self.match_id_history[0]
        response = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/"
                                + recent_match_id + "?api_key=RGAPI-" + self.key)
        participants = response['metadata']['participants']
        summoner_place = 0
        for participant in participants:
            if str(participant) == self.puuid:
                break
            summoner_place += 1
        participant_info = response['info']['participants'][summoner_place]
        recent_champion = str(participant_info['championName'])
        recent_position = str(participant_info['individualPosition'])
        recent_kills = str(participant_info['kills'])
        recent_deaths = str(participant_info['deaths'])
        recent_assists = str(participant_info['deaths'])
        recent_win = str(participant_info['win'])
        return_list = [recent_champion, recent_position, recent_kills, recent_deaths, recent_assists,
                       recent_win]
        return return_list