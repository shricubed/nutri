#Discord bot for nutrimatic.org
#Made by shricubed
#Nutrimatic originally created by egnor

import requests
from bs4 import BeautifulSoup
import discord


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content.startswith("!nutri")):
        words = message.split()
        query = words[1]
        URL = "https://nutrimatic.org/?q=" + query + "&go=Go"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('span')
        if (len(words) == 3 and words[2] < len(results)):
            await message.channel.send(results[words[2]].text)
        else:
            for result in results:
                await message.channel.send(result.text)

    elif (message.content == "!help"):
        await message.channel.send("The basic form of command is !nutri [query] [optional index]. Query syntax is on the front page of nutrimatic.org.")

client.run('INSERT TOKEN HERE')



