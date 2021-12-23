# -*- coding: utf-8 -*-

"""
Administrative commands
"""

from argparse import ArgumentParser
from typing import TypeVar

from core.settings import COLOR_ERROR, COLOR_SUCCESS

from nextcord.embeds import Embed
from nextcord.ext import commands
from nextcord.ext.commands.converter import MemberConverter
from nextcord.ext.commands.errors import CommandError, MemberNotFound, MissingPermissions


_CE_contra = TypeVar('_CE_contra', bound='CommandError', contravariant=True)

parser = ArgumentParser()
parser.add_argument('-u', '--user', type=str, nargs=1, default=None)
parser.add_argument('-U', '--users', type=str, nargs='+', default=None)
parser.add_argument('-r', '--reason', type=str, nargs='*', default=['No', 'reason', 'provided'])


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
            `-r` : Specify reason

        Examples:
            `$kick -u @user`
            `$kick --user @user_or_id`
            `$kick -U @user1 @user2`
            `$kick --users @user1 @user2`
            `$kick -u @user -r "reason for kicking"`
            `$kick -U @user1 @user2 -r "reason for kicking"`
        """

        try:
            parsed = parser.parse_args(list(args))
        except SystemExit:
            raise CommandError

        reason = ' '.join(parsed.reason)

        if parsed.user:
            user = await MemberConverter().convert(ctx, parsed.user[0])

            await user.kick(reason=reason)

            eb = Embed(colour=COLOR_SUCCESS, title='User kicked')
            eb.add_field(name='User:', value=f'{user.name}#{user.discriminator} ({user.id})', inline=False)

        elif parsed.users:
            users = []

            for user in parsed.users:
                try:
                    user = await MemberConverter().convert(ctx, user)
                    await user.kick(reason=reason)
                    users.append(f'`{user.name}#{user.discriminator} ({user.id})`')
                except MemberNotFound:
                    users.append(f'Not found! {user}')

            eb = Embed(colour=COLOR_SUCCESS, title='Users kicked')
            eb.add_field(name='Users:', value=f'{chr(10).join(x for x in users)}', inline=False)

        eb.add_field(name='Reason', value=reason)
        await ctx.send(embed=eb)

    @kick.error
    async def kick_error(error: _CE_contra, ctx: commands.Context, *args):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        else:
            eb = Embed(colour=COLOR_ERROR, title='Command error')
            eb.add_field(name='Example 1', value='$kick -u @user_or_id', inline=False)
            eb.add_field(name='Example 2', value='$kick -user @user_or_id', inline=False)
            eb.add_field(name='Example 3', value='$kick -U @user1 @user2 ...', inline=False)
            eb.add_field(name='Example 4', value='$kick -users @user1 @user2 ...', inline=False)
            eb.add_field(name='Example 5', value='$kick -u @user -r "reason for kicking"', inline=False)
            await ctx.send(embed=eb)

    @commands.command(help='Bans an user or group of users')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, *args):

        try:
            parsed = parser.parse_args(list(args))
        except SystemExit:
            raise CommandError

        reason = ' '.join(parsed.reason)

        if parsed.user:
            user = await MemberConverter().convert(ctx, parsed.user[0])

            await user.ban(reason=reason)

            eb = Embed(colour=COLOR_SUCCESS, title='User banned')
            eb.add_field(name='User banned:', value=f'{user.name}#{user.discriminator} ({user.id})', inline=False)

        elif parsed.users:
            users = []

            for user in parsed.users:
                try:
                    user = await MemberConverter().convert(ctx, user)
                    await user.ban(reason=reason)
                    users.append(f'`{user.name}#{user.discriminator} ({user.id})`')
                except MemberNotFound:
                    users.append(f'Not found! {user}')

            eb = Embed(colour=COLOR_SUCCESS, title='Users banned')
            eb.add_field(name='Users banned:', value=f'{chr(10).join(x for x in users)}', inline=False)

        eb.add_field(name='Reason', value=reason)
        await ctx.send(embed=eb)

    @ban.error
    async def ban_error(error: _CE_contra, ctx: commands.Context):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        else:
            eb = Embed(colour=COLOR_ERROR, title='Command error')
            eb.add_field(name='Example 1', value='$ban -u @user_or_id', inline=False)
            eb.add_field(name='Example 2', value='$ban -user @user_or_id', inline=False)
            eb.add_field(name='Example 3', value='$ban -U @user1 @user2 ...', inline=False)
            eb.add_field(name='Example 4', value='$ban -users @user1 @user2 ...', inline=False)
            eb.add_field(name='Example 5', value='$ban -u @user -r "reason for banning"', inline=False)
            await ctx.send(embed=eb)

    # TODO: role_kick, role_ban


def setup(bot: commands.Bot):
    """Initializes and adds the cog to the bot

    This function gets called by `load_extension` in order to load the Cog
    """
    bot.add_cog(Administration(bot))
