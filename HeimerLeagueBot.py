import discord
from DataDragon import DataDragon
from FactSelector import FactSelector
from SummonerInfo import SummonerInfo

client = discord.Client()
select_fact = FactSelector()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('test'):
        await message.channel.send('pickle rick')
    elif message.content.startswith('!fact'):
        await message.channel.send(select_fact.get_fact())
    elif message.content.startswith('!Champion '):
        input = message.content
        try:
            select_dataDragon = DataDragon(input)
            output = select_dataDragon.getChampData()
            await message.channel.send(output)
        except Exception:
            await message.channel.send("Invalid Champion Name")
    elif message.content.startswith('!Stat '):
        input = message.content
        try:
            select_dataDragon = DataDragon(input)
            output = select_dataDragon.getStats()
            await message.channel.send(output)
        except Exception:
            await message.channel.send("Invalid Champion Name")
    elif message.content.startswith('!SummonerInfo '):
        input = message.content
        try:
            select_summoner_info = SummonerInfo(input)
            output = select_summoner_info.get_level()
            await message.channel.send(str(output[0]) + ": Level " + str(output[1]))
        except Exception:
            await message.channel.send("Invalid Summoner Name")
    elif message.content.startswith('!MatchHistory '):
        input = message.content
        try:
            select_summoner_info = SummonerInfo(input)
            output = select_summoner_info.get_most_recent_match_info()
            await message.channel.send(output[5] + " as " + output[0] + " " + output[1]
                                       + '\n' + " KDA: " + output[2] + "/" + output[3] + "/" + output[4])
        except Exception:
            await message.channel.send("Invalid Summoner Name")
    elif message.content.startswith('!Winrate '):
        input = message.content
        try:
            select_summoner_info = SummonerInfo(input)
            output = select_summoner_info.recent_win_rate()
            await message.channel.send("Win: " + str(output[0]) + '\n' + " Loss: " + str(output[1] - output[0])
                                       + '\n' + " Win rate: " + str(output[0]/output[1]) + "%")
        except Exception:
            await message.channel.send("Invalid Summoner Name")



# uncomment this line and input password
client.run("OTExNTAxMzU5Nzk3Mzg3Mjg1.YZiTyw.AAUNRcmbsqDgsjKWc4frEkWlbCQ")