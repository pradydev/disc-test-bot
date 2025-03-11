import discord
from discord.ext import commands

import os
import asyncio

description = '''simple test bot by prady'''

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
   try:
       synced_cmds = await bot.tree.sync()
       print(f"Synced {len(synced_cmds)} commands")
   except Exception as excp:
       print("Error occured with syncing app commands: ", excp)


async def Load():
   for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
         await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
      async with bot:
         await Load()
         #set token
         await bot.start('')

asyncio.run(main())
