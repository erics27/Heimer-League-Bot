import discord

from FactSelector import FactSelector

client = discord.Client()
select_fact = FactSelector()

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

# uncomment this line and input password
client.run("OTExNTAxMzU5Nzk3Mzg3Mjg1.YZiTyw.AAUNRcmbsqDgsjKWc4frEkWlbCQ")