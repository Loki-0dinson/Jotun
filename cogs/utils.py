# -*- coding: utf-8 -*-

"""
Utility commands
"""

from nextcord.ext import commands

from core.settings import COGS


class Utils(commands.Cog):
    """Cog that groups all the general use commands or that show useful
    information"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Shows latency in ms"""
        await ctx.send(f'{self.bot.latency * 1000:.2f}ms')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def restart(self, ctx):
        """Refreshes all cogs"""
        for cog in COGS:
            self.bot.reload_extension(cog)

        await ctx.send('Done!')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def killbot(self, ctx):
        """Closes the bot"""
        await ctx.send('*Ugh')
        await ctx.send(
            'https://tenor.com/view/dies-cat-dead-died-gif-13827091')
        await self.bot.close()


def setup(bot):
    """Adds the cog to the bot

    This function gets called by `load_extension` in order to load the Cog
    """
    bot.add_cog(Utils(bot))
