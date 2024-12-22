import discord
import asyncio

TOKEN = 'Tokan_bot'  # Replace with your bot token
CHANNEL_ID = "channel ID"  # Replace with your channel ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)  

    if channel:
        while True:
            await channel.send('Your Spamming Massage Here')
            await asyncio.sleep(2)  # Time interval between massages.
    else:
        print("Channel not found. Please check the CHANNEL_ID.")

client.run(TOKEN)

from keep_alive import keep_alive

keep_alive()    
bot.run(TOKEN)
