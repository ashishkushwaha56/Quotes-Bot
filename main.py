import discord
import os
import requests
import json
from keep_alive import keep_alive


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
  
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

my_secret = os.environ['TOKEN']

keep_alive()
client.run(my_secret)