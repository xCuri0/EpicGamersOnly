#!/usr/bin/python3
"""
Epic Gamers Only
"""
import os
import discord
from discord.ext import commands

ALLOWED = ['Minecraft', 'Roblox', 'Badlion Client']
bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print("Bot running")
    activity = discord.Activity(name="Mineblox", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)


@bot.event
async def on_member_update(before, after):
    if not after.activity:
        return
    if after.activity.name == 'Fortnite':
        await after.send("%s FUCK OFF FAGNITE PLAYER" % after.mention)
    elif not after.activity.name in ALLOWED:
        await after.send("%s YOU CANNOT PLAY %s ON %s" % (after.mention, \
                                                        after.activity.name.upper(), \
                                                        after.guild.name.upper()))

if __name__ == "__main__":
    bot.run(os.environ['TOKEN'])
