import os
import discord
from discord.ext import commands
import random
import logging
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

description = '''A great guy who handles stuff you'd want to do during an RPG session'''

intents = discord.Intents.default()
intents.message_content = True
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print('----------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('?hello'):
        await message.channel.send('Hello!')

@bot.command()
async def roll(ctx, dice: str):
    '''Rolls dice in NdN format'''
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

bot.run(TOKEN, log_handler=handler)