# -*- coding: utf-8 -*-

"""
Utility commands
"""

from nextcord.ext import commands
from nextcord.member import Member

from core.settings import COGS


class Utilities(commands.Cog):
    """General use commands or commands that show useful information"""
    qualified_name = 'Utilities'

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def ping(self, ctx: commands.Context):
        """Shows latency in ms"""
        await ctx.send(f'{self.bot.latency * 1000:.2f}ms')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def restart(self, ctx: commands.Context):
        """Refreshes all cogs"""
        for cog in COGS:
            self.bot.reload_extension(cog)

        await ctx.send('Done!')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def killbot(self, ctx: commands.Context):
        """Closes the bot"""
        await ctx.send('*Ugh')
        await ctx.send(
            'https://tenor.com/view/dies-cat-dead-died-gif-13827091')
        await self.bot.close()

    @commands.command(aliases=['user', 'infouser', 'ui', 'iu'])
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def user_info(self, ctx: commands.Context, user: Member | None):
        ...


def setup(bot: commands.Bot):
    """Adds the cog to the bot

    This function gets called by `load_extension` in order to load the Cog
    """
    bot.add_cog(Utilities(bot))
