import discord
from  discord import app_commands
from discord.ext import commands
import yt_dlp
import time
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    

    async def play(self, ctx, url):
        yt_dl_options = {'format' : 'bestaudio/best'}
        ytdl = yt_dlp.YoutubeDL(yt_dl_options)
        ffmpeg_options = {'options': "-vn"}

        vc_clients = {}
        try:
            vclient = await ctx.author.voice.channel.connect()
            vclient[vclient.guild.id] = vclient
        except:
            print("connect error")

        try:
            loop = asyncio.get_event_loop
            ytdata = await loop.run_in_executor(None, lambda: ytdl.extract_info(url,download=False))

            song = ytdata[url]
            #set ffmpeg path
            player = discord.FFmpegPCMAudio(song, executable="")
            vclient[ctx.guild.id].play(player)
        except Exception as error:
            print(error)

    async def pause(self, ctx):
        try:
            vclient[ctx.guild.id].pause()
        except Exception as error:
            print(error)
    
    async def resume(self, ctx):
        try:
            vclient[ctx.guild.id].resume()
        except Exception as error:
            print(error)

    async def stop(self, ctx):
        try:
            vclient[ctx.guild.id].stop()
        except Exception as error:
            print(error)

async def setup(bot):
    await bot.add_cog(Music(bot))
