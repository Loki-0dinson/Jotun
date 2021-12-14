# -*- coding: utf-8 -*-

"""
Reusable functions/classes
"""

from typing import Optional, Set
from nextcord.embeds import Embed
from nextcord.ext import commands

from core.settings import COLOR_SUCCESS


class CustomHelpCommand(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.context.clean_prefix, command.qualified_name, command.signature)

    async def _help_embed(
        self,
        title: str,
        description: Optional[str] = None,
        mapping: Optional[dict] = None,
        command_set: Optional[Set[commands.Command]] = None,
        set_author: bool = False
    ) -> Embed:
        embed = Embed(title=title, colour=COLOR_SUCCESS)
        if description:
            embed.description = description
        if set_author:
            avatar = self.context.bot.user.avatar or self.context.bot.user.default_avatar
            embed.set_author(name=self.context.bot.user.name, icon_url=avatar.url)
        if command_set:
            # show help about all commands in the set
            filtered = await self.filter_commands(command_set, sort=True)
            for command in filtered:
                embed.add_field(
                    name=self.get_command_signature(command),
                    value=command.short_doc or "...",
                    inline=False
                )
        elif mapping:
            # add a short description of commands in each cog
            for cog, command_set in mapping.items():
                filtered = await self.filter_commands(command_set, sort=True)
                if not filtered:
                    continue
                cog_name = cog.qualified_name if cog else "No category"
                # \u2002 is an en-space
                cmd_list = " ".join(
                    f"`{self.context.clean_prefix}{cmd.name}`" for cmd in filtered
                )
                value = (
                    f"{cog.description}\n{cmd_list}"
                    if cog and cog.description
                    else cmd_list
                )
                embed.add_field(name=cog_name, value=value)
        return embed

    async def send_bot_help(self, mapping: dict):
        eb = await self._help_embed(
            title='Bot commands',
            description=self.context.bot.description,
            mapping=mapping
        )
        await self.get_destination().send(embed=eb)

    async def send_cog_help(self, cog: commands.Cog):
        eb = await self._help_embed(
            title=cog.qualified_name,
            description=cog.description,
            command_set=cog.get_commands()
        )
        await self.get_destination().send(embed=eb)

    async def send_command_help(self, command: commands.Command):
        eb = await self._help_embed(
            title=command.qualified_name,
            description=command.help
        )
        await self.get_destination().send(embed=eb)