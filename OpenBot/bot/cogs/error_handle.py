import discord
from discord.ext.commands import Cog, Context, errors

class Error_Handler(Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_command_error(self, ctx : Context, e : errors.CommandError):
        print(e)
        if isinstance(e, discord.ext.commands.CommandNotFound):
            await ctx.send("Invalid Command.")

def setup(bot):
    bot.add_cog(Error_Handler(bot))