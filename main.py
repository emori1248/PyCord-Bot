# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands

import requests
# import re

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    # escaped_query = re.escape("https://bot-webapp.vercel.app/api/trpc/rules.getAll?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22guild_id%22%3A%22846599213440696360%22%7D%7D%7D")
    response = requests.get("https://bot-webapp.vercel.app/api/trpc/rules.getAll?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22guild_id%22%3A%22846599213440696360%22%7D%7D%7D")
    print(response)
    await ctx.send(response)

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")


bot.run(os.environ["DISCORD_TOKEN"])
