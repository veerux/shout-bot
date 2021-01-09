import discord
import os
import requests
import pyjokes

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('HELLO!')

  if message.content.startswith('$jj'):
    joke = pyjokes.get_joke()
    await message.channel.send(joke)


client.run(os.getenv('TOKEN'))

