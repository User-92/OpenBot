import discord
from discord.ext import commands

class Role_Assigner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member.name} joined the server!")
        new_role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(new_role)
        
def setup(bot):
    bot.add_cog(Role_Assigner(bot))