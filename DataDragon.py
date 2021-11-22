import string

import requests, json


class DataDragon:

    replaced = False;
    name = ""
    replaced_name = ""
    desc = ""
    champId = ""
    ADbase = 0
    ADpl = 0
    FMS = 0
    ASpl = 0
    title = ""

    def __init__(self, input):
        # Concat input
        index = input.find(" ")
        name = input[index + 1:len(input)]
        name = self.cap_each(name)

        self.name = name
        response = requests.get('http://ddragon.leagueoflegends.com/cdn/11.23.1/data/en_US/champion.json')
        response.json()
        champ_raw_data = json.loads(response.text)
        crd = champ_raw_data['data']

        if " " in self.name:
            self.replaced_name = self.name
            self.name = self.name.replace(" ", "")
            self.replaced = True
        self.desc = crd[self.name]['blurb']
        self.champId = crd[self.name]['id']
        self.ADbase = crd[self.name]['stats']['attackdamage']
        self.ADpl = crd[self.name]['stats']['attackdamageperlevel']
        self.FMS = crd[self.name]['stats']['movespeed']
        self.ASpl = crd[self.name]['stats']['attackspeedperlevel']
        self.title = crd[self.name]['title']
        if self.replaced:
            self.name = self.replaced_name

    def cap_each(self, string):
        list_of_words = string.split(" ")

        for word in list_of_words:
            list_of_words[list_of_words.index(word)] = word.capitalize()

        return " ".join(list_of_words)

    def compactSpaces(self, str):
        os = ""
        for c in str:
            if c != " " or (os and os[-1] != " "):
                os += c
        return os

    def getChampData(self):
        if self.replaced:
            self.name = self.compactSpaces(self.name)
        output = self.name + " " + self.title + " :" + '\n' + self.desc
        return output

    def getStats(self):
        output = self.name + " :" + '\n' + "Base Attack Damage " + str(self.ADbase) + '\n' + "Attack-Damage Per-level " +\
                 str(self.ADpl) + '\n' + "Attack-Speed " + str(self.ASpl) + '\n' + "Attack-Speed " + str(self.FMS)
        return output
