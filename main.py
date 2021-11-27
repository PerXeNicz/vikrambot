#Bot Name: Vikram Rahul Abishek Pranav Rajesh
#Alias: GM VIKRAM

import discord
from discord.utils import get
from discord.ext import commands
#from datetime import datetime, timedelta
from songs import songAPI 

def read_token():
    with open("token.txt", "r") as f:
        lines=f.readlines()
        return lines[0].strip()

discord_token = read_token()

bot = commands.Bot(command_prefix='!',help_command=None)

songsInstance = songAPI()

@bot.event
async def on_ready():
    print(f"Logged In")

@bot.command()
async def chess(ctx):
    await ctx.channel.send("https://i.pinimg.com/originals/ff/dc/94/ffdc948e6807a8fc8c9871edbbbd424c.gif")

@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="Grandmaster Vikram Rahul Abishek Pranav Rajesh will help you.", description="Available commands", color=0x2ACAEA)
    emBed.add_field(name='!play', value="Add a song to queue and plays it.", inline=False)
    emBed.add_field(name='!pause', value="Pauses the currently playing track.", inline=False)
    emBed.add_field(name='!resume', value="Resumes the track you just pause.", inline=False)
    emBed.add_field(name='!skip', value="Skip the current song.", inline=False)
    emBed.add_field(name='!queue', value="Display the queue of the current tracks in the playlist.", inline=False)
    emBed.add_field(name='!leave', value="Kick GM VIKRAM from voice channel.", inline=False)
    emBed.add_field(name='!chess', value="The next move is obvious.", inline=False)
    emBed.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLR75wfNA5EF7VbFGDfirGklxqQ_33TgIBzdiyc2=s88-c-k-c0x00ffffff-no-rj')
    await ctx.channel.send(embed=emBed)

@bot.command() 
async def play(ctx,* ,search: str):
    await songsInstance.play(ctx, search)

@bot.command()
async def pause(ctx):
    await songsInstance.pause(ctx)

@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)

@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)

@bot.command()
async def queue(ctx):
    await songsInstance.queue(ctx)

@bot.command()
async def skip(ctx):
    await songsInstance.skip(ctx)

bot.run(discord_token)