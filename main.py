# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

from db import query_db

import re

ruleset = {}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    ruleset[846599213440696360] = query_db(846599213440696360)

@bot.event
async def on_message(message):
    for rule in (ruleset[message.guild.id]):
        if re.search(rule[2], message.content) != None:
            print("match on " + rule[2])
            await message.delete()
            await message.channel.send("naughty")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def db(ctx):
    print(ctx.guild)
    ruleset[ctx.guild.id] = query_db(ctx.guild.id)
    
    await ctx.send(ruleset[ctx.guild.id])

# @bot.command()
# async def test(ctx):
#     print("ruleset:")
#     print(ruleset[ctx.guild.id])


bot.run(os.environ["DISCORD_TOKEN"])
