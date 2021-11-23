import os
import requests
import json


class SummonerInfo:

    key = str(os.environ.get("RIOT_API_KEY"))
    summoner_name = ""
    no_spaces_summoner_name = ""
    puuid = ""
    match_id_history = []

    def __init__(self, sum_name):
        self.summoner_name = self.concat_name(sum_name)
        self.no_spaces_summoner_name = self.summoner_name.replace(" ", "%20")
        self.puuid = self.get_puuid()
        self.match_id_history = self.get_match_id_history()

    def concat_name(self, sum_name):
        index = sum_name.find(" ")
        ret_name = sum_name[index + 1:len(sum_name)]
        return ret_name

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
        match_data = json.loads(response.text)
        participants = match_data['metadata']['participants']
        summoner_place = self.get_summoner_place_from_match(participants)
        participant_info = match_data['info']['participants'][summoner_place]

        recent_champion = str(participant_info['championName'])
        recent_position = str(participant_info['individualPosition'])
        if recent_position == 'Invalid':
            recent_position = 'ARAM'
        recent_kills = str(participant_info['kills'])
        recent_deaths = str(participant_info['deaths'])
        recent_assists = str(participant_info['assists'])
        if participant_info['win']:
            recent_win = "Win"
        else:
            recent_win = "Loss"
        return_list = [recent_champion, recent_position, recent_kills, recent_deaths, recent_assists,
                       recent_win]
        return return_list

    def recent_win_rate(self):
        recent_match_ids = self.match_id_history
        wins = 0.0
        games = 0.0
        for recent_match_id in recent_match_ids:
            response = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/"
                                    + recent_match_id + "?api_key=RGAPI-" + self.key)
            match_data = json.loads(response.text)
            status_in_match_data = "status" in match_data
            if not status_in_match_data:
                participants = match_data['metadata']['participants']
                summoner_place = self.get_summoner_place_from_match(participants)
                participant_info = match_data['info']['participants'][summoner_place]
                if participant_info['win']:
                    wins += 1
                games += 1
            print(str(wins) + " " + str(games))
        return_list = [wins, games]
        return return_list

    def get_summoner_place_from_match(self, participants):
        summoner_place = 0
        for participant in participants:
            if str(participant) == self.puuid:
                break
            summoner_place += 1
        return summoner_place
