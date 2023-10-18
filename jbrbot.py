import discord
import g4f
import os
import asyncio
from icecream import ic
intents = discord.Intents.all()
client = discord.Client(intents=intents)

g4f.logging = True

channel = client.get_channel(1163973446779273308)
TOKEN = "MTE2MzYxODk5NjM4NjU0MTYwOQ.G1CUT-.yAuuLD7goo0FY2Q-jSl0gMxrbDDejnNT8OeG7s"

@client.event
async def on_ready():
  print(f"Bot {client.user} is online!!")
  # await msg.channel.send("The ChatGPT bot is alive.")

@client.event
async def on_message(msg):
  guild = msg.channel.guild
  channel = msg.channel
  if msg.author == client.user:
    return
  conversation = [{
    "role": "system",
    "content": "Hello ChatGPT!"
  }]
  cont = msg.content
  print(f"user {msg.author} messaged: {cont}")
  conversation.append({
    "role": "user",
    "content": cont  
  })
  await msg.channel.send("The bot is typing...")
  response = g4f.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages= conversation,
    stream = True
  )
  
  stack = []
  str = ""
  for messages in response:
    str += messages
    stack.append(str)
      
  a = stack.pop()
  print(a)
  await msg.channel.send(a, reference=msg)
  print(response)

client.run(TOKEN)