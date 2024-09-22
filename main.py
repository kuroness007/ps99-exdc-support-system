import discord
import os
#import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    emoji ="👍"
    await message.add_reaction(emoji)

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
#keep_alive()
client.run(TOKEN)