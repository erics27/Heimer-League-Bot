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

    if message.content.startswith('test'):
        await message.channel.send('pickle rick')
    elif message.content.startswith('!fact'):
        await message.channel.send(select_fact.get_fact())

# uncomment this line and input password
client.run("OTExNTAxMzU5Nzk3Mzg3Mjg1.YZiTyw.rFc6ynX4hEeAMnbwKhckGIHol8A")