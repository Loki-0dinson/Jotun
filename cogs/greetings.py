from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *args, **kwargs):
        await ctx.send('Hello')


def setup(bot):
    bot.add_cog(Greetings(bot))
