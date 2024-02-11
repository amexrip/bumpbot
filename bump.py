import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)
loop_count = 0
channel_id = ### PUT CHANNEL ID HERE ###

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    bot.loop.create_task(bump_every_2_hours())

async def bump():
    global loop_count
    channel = bot.get_channel(channel_id)
    await channel.send('/bump')
    loop_count += 1

async def bump_every_2_hours():
    while True:
        t = loop_count * 59  
        await asyncio.sleep(2 * 60 * 60 + t)
        await bump()

### TOKEN HERE  \/\/\/ ###
bot.run('your_bot_token')
