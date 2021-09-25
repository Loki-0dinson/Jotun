# -*- coding: utf-8 -*-

"""
Database class for the bot.
"""

import logging

from nextcord import Game
from nextcord.ext import commands
from nextcord.ext.commands.errors import CommandNotFound

from core.settings import TOKEN, DEBUG, LOG_LEVEL, LOG_FORMAT, \
    LOG_DATE_FORMAT, COGS

if DEBUG:
    from icecream import ic  # pylint: disable=W0611


###############################################################################
# Logging
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, style='{')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Bot stuff
bot = commands.Bot(command_prefix='$', activity=Game(name='$help'))
###############################################################################


async def get_prefix(message):
    """Retrieves the prefix the bot is listening to with the message as a
    context.

    Args:
        bot (nexcord.commands.Bot): The instance of
        message (nextcord.Message): The message context to get the prefix of.

    Returns:
        Union[List[str], str]: A list of prefixes or a single prefix that the
        bot is listening for.

    https://nextcord.readthedocs.io/en/latest/ext/commands/api.html?#nextcord.ext.commands.Bot.get_prefix
    """
    prefixes = ['$']

    # # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow $ to be used in DMs
        return '$'

    # If we are in a guild, we allow for the user to mention us or use any of
    # the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


@bot.event
async def on_ready():
    """Called when the client is done preparing the data received from Discord.
    Usually after login is successful and the Client.guilds and co. are filled
    up.

    https://nextcord.readthedocs.io/en/latest/api.html#nextcord.on_ready
    """
    logger.info('Logged in as: NAME %s, ID %i', bot.user.name, bot.user.id)


@bot.event
async def on_message_delete(message):
    """Called when a message is deleted. If the message is not found in the
    internal message cache, then this event will not be called. Messages might
    not be in cache if the message is too old or the client is participating in
    high traffic guilds.

    If this occurs increase the Client.max_messages attribute or use the
    `on_raw_message_delete()` event instead.

    This requires Intents.messages to be enabled.

    Args:
        message (str): The deleted message.

    https://nextcord.readthedocs.io/en/latest/api.html#nextcord.on_message_delete
    """
    return message


@bot.event
async def on_command_error(_, error):
    """Command error handler.

    https://nextcord.readthedocs.io/en/latest/ext/commands/api.html?#nextcord.ext.commands.Bot.on_command_error
    """
    if isinstance(error, CommandNotFound):
        return
    raise error


if __name__ == '__main__':
    logger.info('Loading cogs')
    for cog in COGS:
        bot.load_extension(cog)

    logger.info('Running bot')
    bot.run(TOKEN)
