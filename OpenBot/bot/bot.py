import discord, os
from discord.ext import commands, tasks

with open("token.txt", "r") as tokenfile:
    token = tokenfile.read()
    tokenfile.close()

class Bot(commands.Bot):
    """discord.ext.commands.Bot subclass"""
    def __init__(self, command_prefix, activity):
        super().__init__(command_prefix)
        self.activity = activity

    def load_cogs(self):
        """load all cogs"""
        for cog in [file.split(".")[0] for file in os.listdir("cogs") if file.endswith(".py")]:
            try:
                if cog != "__init__":
                    self.load_extension(f"cogs.{cog}")
            except Exception as ex:
                print(ex)

    def add_cog(self, cog : commands.Cog):
        """add a cog to the bot"""
        super().add_cog(cog)

    async def on_ready(self):
        """
        When the bot is ready to run, the cogs are loaded and sends a message to say that the bot is running
        """
        self.load_cogs()
        await super().change_presence(activity=self.activity)
        print("Bot Prepared!")

bot = Bot(command_prefix="!",
          activity=discord.Game(name="Commands: !commands"))
bot.run(token)