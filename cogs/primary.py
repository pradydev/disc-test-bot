import discord
from  discord import app_commands
from discord.ext import commands

class Primary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('[][][][][]')

    @commands.command()
    async def stats(self, ctx):
        stat_embed = discord.Embed(title=f"Clementine and {ctx.guild.name} stats", description="stats", color=discord.Color.orange())
        stat_embed.add_field(name=f"Clementine latency (ms): ", value=f"{round(self.bot.latency*1000)}ms.", inline=True)
        stat_embed.add_field(name=f"Server members: ", value=f"{ctx.guild.member_count}", inline=True)

   
        stat_embed.set_footer(text=f"Command sent by {ctx.author.name}", icon_url=ctx.author.avatar)


        await ctx.send(embed=stat_embed)

    @app_commands.command(name="stats", description="displays bot and server stats")
    async def stats(self, interaction: discord.Interaction):
        stat_embed = discord.Embed(title=f"Clementine and {interaction.guild.name} stats", description="stats", color=discord.Color.orange())
        stat_embed.add_field(name=f"Clementine latency (ms): ", value=f"{round(self.bot.latency*1000)}ms.", inline=True)
        stat_embed.add_field(name=f"Server members: ", value=f"{interaction.guild.member_count}", inline=True)

   
        stat_embed.set_footer(text=f"Command sent by {interaction.author.name}", icon_url=interaction.author.avatar)


        await interaction.response.send_message(embed=stat_embed)

async def setup(bot):
    await bot.add_cog(Primary(bot))
