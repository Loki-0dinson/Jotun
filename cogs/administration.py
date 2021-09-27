# -*- coding: utf-8 -*-

"""
Administrative commands
"""

from typing import TypeVar
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, Context, Bot
from nextcord.ext.commands.errors import CommandError, MissingPermissions
from nextcord.member import Member


_CE_contra = TypeVar('_CE_contra', bound='CommandError', contravariant=True)


class Administration(commands.Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx: Context, user: Member = None, reason: str = ''):
        await self.bot.kick(user, reason=reason)
        await ctx.send((user, reason))

    @kick.error
    async def kick_error(error: _CE_contra, ctx: Context):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        else:
            await ctx.send(error, type(error))

    @commands.command
    @has_permissions(ban_members=True)
    async def ban(self, ctx: Context, user: Member = None, reason: str = ''):
        await self.bot.ban(user, reason=reason)
        await ctx.send((user, reason))

    @kick.error
    async def ban_error(error: _CE_contra, ctx: Context):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        else:
            await ctx.send(error, type(error))


def setup(bot: Bot):
    """Initializes and adds the cog to the bot

    This function gets called by `load_extension` in order to load the Cog
    """
    bot.add_cog(Administration(bot))
