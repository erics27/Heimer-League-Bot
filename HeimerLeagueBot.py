import discord
import random

from FactSelector import FactSelector

client = discord.Client()
select_fact = FactSelector()

coin = ("heads", "tails")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!fact'):
        await message.channel.send(select_fact.get_fact())
    elif message.content.startswith('!help'):
        await message.channel.send('!fact = Gives a random league fact')
    elif message.content.startswith('!coinflip'):
        await message.channel.send(random.choice(coin))

# uncomment this line and input password
client.run("OTExNTAxMzU5Nzk3Mzg3Mjg1.YZiTyw.AAUNRcmbsqDgsjKWc4frEkWlbCQ")