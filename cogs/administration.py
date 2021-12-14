# -*- coding: utf-8 -*-

"""
Administrative commands
"""

from typing import TypeVar
from nextcord.embeds import Embed
from nextcord.ext import commands
from nextcord.ext.commands.errors import CommandError, MissingPermissions
from nextcord.member import Member

from core.settings import COLOR_ERROR, COLOR_SUCCESS


_CE_contra = TypeVar('_CE_contra', bound='CommandError', contravariant=True)


class Administration(commands.Cog):
    """Moderation and server administration commands"""
    qualified_name = 'Administration'

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, *args):
        """Kicks an user or group of users works with both mentions or user id

            `-u` : specify single user
            `-U` : specify ultiple users
            `-r` : Specify reason (must use quotation marks)

        Examples:
            `$kick @user_or_id`
            `$kick @user1 @user2`
            `$kick -u @user`
            `$kick -U @user1 @user2`
            `$kick -u @user -r "reason for kicking"`
            `$kick -U @user1 @user2 -r "reason for kicking"`
        """

        # TODO: delet dis, use shlex + argparse
        match args:
            case ['-u', user]:
                await Member(user).kick(reason='No reason provided')

            case ['-U', *users, '-r', reason] | ['-r', reason, '-U', *users]:
                for user in users:
                    await Member(user).kick(reason=reason)

            case ['-u', user, '-r', reason] | [user, reason] | ['-r', reason, '-u', user]:
                await Member(user).kick(reason=reason)

            case ['-U', *users] | [*users]:
                for user in users:
                    await Member(user).kick(reason='No reason provided')
            case _:
                raise CommandError()

        eb = Embed(colour=COLOR_SUCCESS, title='User kicked',
            description=f'User: `{user.name}#{user.discriminator}` \
                `({user.id})`\nReason: {reason}'
        )
        await ctx.send(embed=eb)

    @kick.error
    async def kick_error(error: _CE_contra, ctx: commands.Context, *args):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        else:
            eb = Embed(colour=COLOR_ERROR, title='Command error')
            eb.add_field(name='Example 1', value='$kick -u @user_or_id')
            eb.add_field(name='Example 2', value='$kick -U @user1 @user2')
            eb.add_field(name='Example 3', value='$kick -u @user -r "reason for kicking"')
            await ctx.send(embed=eb)

    @commands.command(help='Bans an user or group of users')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, user: Member = None, *args):
        if not user:
            eb = Embed( colour=COLOR_ERROR, title='Missing user!',
                description='Usage: `$ban [@user or id] [reason]`')
            return await ctx.send(embed=eb)

        reason = 'No reason provided' if not args else ' '.join(args)

        await user.ban(reason=reason)
        eb = Embed(colour=COLOR_SUCCESS, title='User banned',
            description=f'User: `{user.name}#{user.discriminator}` \
                `({user.id})`\nReason: {reason}'
        )
        await ctx.send(embed=eb)

    @ban.error
    async def ban_error(error: _CE_contra, ctx: commands.Context):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        else:
            await ctx.send(error, type(error))


def setup(bot: commands.Bot):
    """Initializes and adds the cog to the bot

    This function gets called by `load_extension` in order to load the Cog
    """
    bot.add_cog(Administration(bot))
