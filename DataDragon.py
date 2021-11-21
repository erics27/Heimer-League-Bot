import requests, json

response = requests.get('http://ddragon.leagueoflegends.com/cdn/11.23.1/data/en_US/champion.json')
response.json()
champRawData = json.loads(response.text)
crd = champRawData['data']
replaced = False;
replaced_name = ""
# Setting Variables
name = input("What Champion Would you like?")
if (" " in name):
    replaced_name = name
    name = name.replace(" ", "")
    replaced = True
desc = crd[name]['blurb']
champId = crd[name]['id']
ADbase = crd[name]['stats']['attackdamage']
ADpl = crd[name]['stats']['attackdamageperlevel']
FMS = crd[name]['stats']['movespeed']
ASpl = crd[name]['stats']['attackspeedperlevel']
title = crd[name]['title']
if replaced:
    name = replaced_name

def getChampData():
    output = name + " " + title + '\n' + desc
    return output

def getStats():
    output = name + " :" + '\n' + "Base Attack Damage " + str(ADbase) + '\n' + "Attack-Damage Per-level " +\
             str(ADpl) + '\n' + "Attack-Speed " + str(ASpl)
    return output
