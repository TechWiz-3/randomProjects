import discord
import asyncio
import random
import aiohttp
import json
import requests
from dotenv import load_dotenv
import os
bot = discord.Bot()

load_dotenv()
token = os.getenv("token")



# Note: If you want you can use commands.Bot instead of discord.Bot
# Use discord.Bot if you don't want prefixed message commands

# With discord.Bot you can use @bot.command as an alias
# of @bot.slash_command but this is overridden by commands.Bot


@bot.slash_command(guild_ids=[864438892736282625])  # create a slash command for the supplied guilds
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    await ctx.respond(f"Hello {ctx.author}!")

@bot.slash_command(guild_ids=[864438892736282625])
async def newyeargoal(ctx,*,goal):
    await ctx.respond(f"Yessir\nYour goal is `{goal}`")


# @bot.slash_command(guild_ids=[...])
# async def joined(
#     ctx, member: discord.Member = None
# ):  # Passing a default value makes the argument optional
#     user = member or ctx.author
#     await ctx.respond(
#         f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}"
#     )
bot.run(token)