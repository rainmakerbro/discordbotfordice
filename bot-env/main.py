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

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description=description, intents=intents) # commands.when_mentioned_or("!") is used to make the bot respond to !ping and @bot ping

async def setup_hook() -> None: # This function is automatically called before the bot starts
    await bot.tree.sync() # Needed for syncing slash commands with discord

bot.setup_hook = setup_hook

bot.event
async def on_ready() -> None: # called when the bot is ready
    print(f'Logged in as {bot.user}')
    print('----------')

@bot.tree.command()
async def ping(inter: discord.Interaction) -> None:
    await inter.response.send_message(f'> Pong! {round(bot.latency * 1000)}ms')

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