import discord, time
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["commands"])
    async def _commands(self, ctx):
        await ctx.send("Only !commands and !DDoS.")
        
    @commands.command()
    async def DDoS(self, ctx, member : discord.User):
        await ctx.send(f"DDoSing: {member.name}")
        time.sleep(3)
        await ctx.send(f"DDoS complete!")

def setup(bot):
    bot.add_cog(Utils(bot))